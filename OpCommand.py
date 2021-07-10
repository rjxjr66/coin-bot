from Database import db

def opTest(id, today, args):
  return "OP"

def giveMoney(id, today, args):
  otherId, amt = args
  otherId = bytes(otherId, encoding='utf-8')
  if otherId in db.keys():
    amt = int(amt)
    db[otherId]['money'] += amt
    db[otherId] = db[otherId]
    return "입금됐다 휴먼"
  else:
    return "계좌번호 확인해라 휴먼"


def stealMoney(id, today, args):
  otherId, amt = args
  otherId = bytes(otherId, encoding='utf-8')
  if otherId in db.keys():
    amt = int(amt)
    db[otherId]['money'] -= amt
    db[otherId] = db[otherId]
    return "출금됐다 휴먼"
  else:
    return "계좌번호 확인해라 휴먼"

def lockCoin(id, today, args):
  if 'lock' not in db.keys():
    db['lock'] = {}

  db['lock'][args[0]] = True
  db['lock'] = db['lock']

  return "잠금됐다"

def unlockCoin(id, today, args):
  if 'lock' in db.keys() and db['lock'][args[0]]:
    del db['lock'][args[0]]
    db['lock'] = db['lock']

    return '해금됐다'

  return '잠금되어있지않다'
