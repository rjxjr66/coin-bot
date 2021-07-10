import redis
import json

class Database:
  def __init__(self):
    self.db = redis.StrictRedis(host='db', port=6379, db=0)
    self.cache = {}

  def keys(self):
    return self.db.keys()

  def __getitem__(self, key):
    if key in self.cache:
      return self.cache[key]
    
    self.cache[key] = json.loads(self.db.get(key))
    return self.cache[key]

  def __setitem__(self, key, value):
    self.db.set(key, json.dumps(value, indent=2).encode('utf-8'))

  def delete(self, key):
    del self.cache[key]
    self.db.delete(key)

db = Database()