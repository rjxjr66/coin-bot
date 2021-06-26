class Database:
  def __init__(self):
    self.db = {}

  def keys(self):
    return self.db.keys()

  def __getitem__(self, key):
    return self.db[key]

  def __setitem__(self, key, value):
    self.db[key] = value

  def __del__(self, key):
    del self.db[key]

db = Database()