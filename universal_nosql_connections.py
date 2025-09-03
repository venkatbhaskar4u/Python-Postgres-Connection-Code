# MongoDB
def test_mongodb():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")
    db = client["testdb"]
    coll = db["testcollection"]
    coll.insert_one({"test_key": "test_value"})
    result = coll.find_one({"test_key": "test_value"})
    print("MongoDB connection works:", result is not None)
    coll.delete_many({"test_key": "test_value"})

# Cassandra
def test_cassandra():
    from cassandra.cluster import Cluster
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute("CREATE KEYSPACE IF NOT EXISTS testks WITH replication = {'class':'SimpleStrategy','replication_factor' : 1};")
    session.set_keyspace("testks")
    session.execute("CREATE TABLE IF NOT EXISTS testtab (id int PRIMARY KEY, val text);")
    session.execute("INSERT INTO testtab (id, val) VALUES (1, 'abc');")
    rows = session.execute("SELECT * FROM testtab WHERE id=1;")
    found = any(row.val == 'abc' for row in rows)
    print("Cassandra connection works:", found)
    session.execute("DROP TABLE testtab;")

# Redis
def test_redis():
    import redis
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('test_key', 'test_value')
    value = r.get('test_key')
    print("Redis connection works:", value == b'test_value')
    r.delete('test_key')

# DynamoDB (AWS)
def test_dynamodb():
    import boto3
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = "test_table"
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'N'}],
            ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
        )
        table.wait_until_exists()
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        table = dynamodb.Table(table_name)
    table.put_item(Item={'id': 1, 'val': "abc"})
    response = table.get_item(Key={'id': 1})
    print("DynamoDB connection works:", 'Item' in response)
    table.delete_item(Key={'id': 1})
    # table.delete() # Uncomment to clean up the test table

# Couchbase
def test_couchbase():
    from couchbase.cluster import Cluster, ClusterOptions
    from couchbase.auth import PasswordAuthenticator
    # Replace credentials and server address as needed
    cluster = Cluster('couchbase://localhost', ClusterOptions(PasswordAuthenticator('username', 'password')))
    bucket = cluster.bucket('testbucket')
    coll = bucket.default_collection()
    coll.upsert('test_key', {'val': 'value'})
    result = coll.get('test_key').content_as[dict]
    print("Couchbase connection works:", result.get('val') == 'value')
    coll.remove('test_key')

# Elasticsearch
def test_elasticsearch():
    from elasticsearch import Elasticsearch
    es = Elasticsearch("http://localhost:9200")
    doc = {"val": "value"}
    es.index(index="testidx", id=1, document=doc)
    result = es.get(index="testidx", id=1)
    print("Elasticsearch connection works:", result['_source']['val'] == 'value')
    es.delete(index="testidx", id=1)
    es.indices.delete(index="testidx", ignore=[400, 404])

# Firestore (Google Cloud)
def test_firestore():
    from google.cloud import firestore
    db = firestore.Client()
    doc_ref = db.collection(u'test_collection').document(u'test_doc')
    doc_ref.set({'val': u'value'})
    result = doc_ref.get().to_dict()
    print("Firestore connection works:", result.get('val') == 'value')
    doc_ref.delete()

if __name__ == "__main__":
    test_mongodb()
    test_cassandra()
    test_redis()
    # Uncomment as needed for your environment and credentials:
    # test_dynamodb()
    # test_couchbase()
    # test_elasticsearch()
    # test_firestore()
