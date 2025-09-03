# MongoDB
def test_mongodb():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")
    db = client["testdb"]
    coll = db["testcollection"]
    # Insert a doc then find it
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

if __name__ == "__main__":
    test_mongodb()
    test_cassandra()
    test_redis()
