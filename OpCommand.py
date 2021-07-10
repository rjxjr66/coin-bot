from Database import db

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

def bankruptcy(id, today, args):
  otherId = args[0]
  bOtherId = bytes(args[0], encoding='utf-8')
  if bOtherId in db.keys() and otherId in db['bankrupt']:
    del db['bankrupt'][otherId]
    db.delete(bOtherId)
    return "파산됐다 휴먼"
  else:
    return "계좌번호 확인해라 휴먼"

def bankruptcylist(id, today, args):
  if 'bankrupt' not in db.keys():
    db['bankrupt'] = {}

  return [ id for id in db['bankrupt'].keys() ]