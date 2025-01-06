import redis

db = None

def initialize_db():
    global db
    db = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

def get_db():
    return db
