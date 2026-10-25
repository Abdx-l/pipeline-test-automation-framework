from fastapi import FastAPI,HTTPException,Depends,Header,Response
from pydantic import BaseModel,Field
import os
app=FastAPI();records={};sequence=0
M=os.getenv("MUTATION","")
class Policy(BaseModel):name:str=Field(min_length=1);coverage:float=Field(gt=0)
def auth(authorization:str|None=Header(default=None)):
 if authorization!="Bearer local-test-token" and M!="auth":raise HTTPException(401,"unauthorized")
@app.get("/health")
def health():return {"status":"ok"}
@app.post("/policies",dependencies=[Depends(auth)])
def create(p:Policy,response:Response):
 global sequence
 sequence+=1;record={"id":sequence,**p.model_dump()};records[sequence]=record;response.status_code=200 if M=="status" else 201
 if M=="schema":return {"id":sequence}
 return record
@app.get("/policies",dependencies=[Depends(auth)])
def list_(page:int=0,size:int=10):
 if page<0 or not 1<=size<=100:raise HTTPException(400,"invalid page")
 rows=list(records.values());start=(page+1 if M=="paging" else page)*size
 return rows[start:start+size]
@app.get("/policies/{id}",dependencies=[Depends(auth)])
def get(id:int):
 if id not in records:raise HTTPException(404)
 return records[id]
@app.delete("/policies/{id}",dependencies=[Depends(auth)],status_code=204)
def delete(id:int):
 if id not in records:raise HTTPException(404)
 if M!="delete":del records[id]
 return Response(status_code=204)
