import redis
import json

class Database:
  def __init__(self):
    self.db = redis.StrictRedis(host='localhost', port=6379, db=0)

  def keys(self):
    return self.db.keys()

  def __getitem__(self, key):
    return json.loads(self.db.get(key))

  def __setitem__(self, key, value):
    self.db.set(key, json.dumps(value, indent=2).encode('utf-8'))

  def __del__(self, key):
    self.db.delete(key)

db = Database()