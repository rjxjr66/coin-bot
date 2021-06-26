from Database import db
import requests

def getPrice(id, today, args):
  res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={args[0]}&vs_currencies=krw")

  if 400 <= res.status_code < 500:
    return "코인 아이디를 확인해라."
  elif res.status_code >= 500:
    return "코인 가격을 가져올 수 없다."

  return res.json()[args[0]]['krw']

def buy(id, today, args):
  coinId, amount = args[0], int(args[1])
  if 'lock' in db.keys() and coinId in db['lock']:
    return "잠겨있다"

  if db[id]['money'] < amount:
    return "너 거지다 휴먼"

  res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coinId}&vs_currencies=krw")

  if 400 <= res.status_code < 500:
    return "코인 아이디를 확인해라."
  elif res.status_code >= 500:
    return "코인 가격을 가져올 수 없다."

  price = res.json()[coinId]['krw']
  nCoins = amount / price
  if coinId in db[id]['coins']:
    db[id]['coins'][coinId] += nCoins
  else:
    db[id]['coins'][coinId] = nCoins
  db[id]['money'] -= amount

  db[id] = db[id]

  return "매수되었다 휴먼"

  

def sell(id, today, args):
  coinId, amount = args[0], float(args[1])
  if 'lock' in db.keys() and coinId in db['lock']:
    return "잠겨있다"

  if coinId not in db[id]['coins'] or db[id]['coins'][coinId] < amount:
    return '너 거지다 휴먼'

  res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coinId}&vs_currencies=krw")

  if 400 <= res.status_code < 500:
    return "코인 아이디를 확인해라."
  elif res.status_code >= 500:
    return "코인 가격을 가져올 수 없다."

  price = res.json()[coinId]['krw']
  krw = price * amount
  db[id]['money'] += krw
  db[id]['coins'][coinId] -= amount

  return "매도되었다 휴먼"
