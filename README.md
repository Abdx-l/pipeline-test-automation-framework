# Pipeline Test Automation Framework

YAML-driven HTTP scenarios, Dockerized target service, pytest-xdist workers, one-time failure reruns with flaky-result recording, GitLab lint/test/report stages and Allure artifacts.

## Run

Install requirements.txt; `pytest -n 4 --reruns 1 --alluredir=allure-results`. Each worker starts its own local target. Set TARGET_URL for a deployed target. GitLab CI publishes JUnit and Allure raw results.
