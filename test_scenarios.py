import yaml,pytest
from pathlib import Path
CASES=yaml.safe_load(Path(__file__).with_name("cases.yaml").read_text())
@pytest.mark.parametrize("case",CASES,ids=lambda c:c["name"])
def test_scenario(api,case):
 session,base=api;last_id=None
 for step in case["steps"]:
  url=base+step["path"].replace("{id}",str(last_id));response=session.request(step["method"],url,json=step.get("json"),timeout=5)
  assert response.status_code==step["status"],response.text
  if response.status_code==201:last_id=response.json()["id"]
