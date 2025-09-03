# Apache Airflow (REST API example; requires Airflow REST API enabled)
def test_airflow():
    import requests
    airflow_url = "http://localhost:8080/api/v1"
    dag_id = "example_dag"
    response = requests.get(f"{airflow_url}/dags/{dag_id}")
    print("Airflow connection works:", response.status_code == 200)

# Talend (invoking Talend job via REST, example)
def test_talend():
    import requests
    talend_url = "http://localhost:8080/talend/job_service/jobs"
    job_name = "sampleJob"
    response = requests.get(f"{talend_url}/{job_name}/status")
    print("Talend connection works:", response.status_code == 200 or response.status_code == 404) # 404 if not found, shows connection

# Pentaho (PDI/Kettle - running transformation via command line)
def test_pentaho():
    import subprocess
    # Example transform filename
    result = subprocess.run(['kitchen.sh', '/file:/home/user/sample_transform.ktr'], capture_output=True)
    print("Pentaho (Kettle) command run:", result.returncode == 0)

# dbt (data build tool) - test run via subprocess
def test_dbt():
    import subprocess
    result = subprocess.run(['dbt', 'run'], capture_output=True)
    print("dbt CLI run:", result.returncode == 0)

# Prefect (workflow engine API)
def test_prefect():
    import requests
    prefect_url = "http://localhost:4200"
    response = requests.get(prefect_url)
    print("Prefect connection works:", 200 <= response.status_code < 300)

if __name__ == "__main__":
    # Uncomment as needed based on your setup
    # test_airflow()
    # test_talend()
    # test_pentaho()
    # test_dbt()
    # test_prefect()
