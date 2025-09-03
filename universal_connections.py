import pandas as pd

# PostgreSQL
def test_postgres():
    import sqlalchemy
    engine = sqlalchemy.create_engine("postgresql+psycopg2://user:password@host:port/dbname")
    df = pd.read_sql("SELECT 1 as result", engine)
    print("PostgreSQL connection works:", df.result.iloc[0] == 1)

# MySQL
def test_mysql():
    import sqlalchemy
    engine = sqlalchemy.create_engine("mysql+pymysql://user:password@host:port/dbname")
    df = pd.read_sql("SELECT 1 as result", engine)
    print("MySQL connection works:", df.result.iloc[0] == 1)

# SQLite
def test_sqlite():
    engine = sqlalchemy.create_engine("sqlite:///test.db")
    df = pd.read_sql("SELECT 1 as result", engine)
    print("SQLite connection works:", df.result.iloc[0] == 1)

# BigQuery
def test_bigquery():
    from google.cloud import bigquery
    client = bigquery.Client()
    query = "SELECT 1 as result"
    df = client.query(query).to_dataframe()
    print("BigQuery connection works:", df.result.iloc[0] == 1)

# AWS Redshift
def test_redshift():
    import sqlalchemy
    engine = sqlalchemy.create_engine("redshift+psycopg2://user:password@hostname:5439/dbname")
    df = pd.read_sql("SELECT 1 as result", engine)
    print("Redshift connection works:", df.result.iloc[0] == 1)

# Requests API (JSON/REST)
def test_api():
    import requests
    response = requests.get("https://api.github.com")
    print("API connection works:", response.status_code == 200)

if __name__ == "__main__":
    # Uncomment based on available credentials and installed libraries
    # test_postgres()
    # test_mysql()
    # test_sqlite()
    # test_bigquery()
    # test_redshift()
    test_api()
