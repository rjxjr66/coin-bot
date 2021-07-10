from Database import db

def attend(id, today, args):
  if id in db.keys():
    balance = db[id]
    if balance["lastAttendDate"] != today:
      db[id] = {
        "money": balance["money"]+ 5000,
        "lastAttendDate": today,
        "coins": balance["coins"]
      }
      return '출석됐다 휴먼'
    else:
      return '이미 출석했다 휴먼'
  else:
    db[id] = {
      "money": 5000,
      "lastAttendDate": today,
      "coins": {}
    }

    return '출석됐다 휴먼'

def balance(id, today, args):
  msg = []
  if id in db.keys():
    msg.append(f"원화: {db[id]['money']}원")
    for key, value in db[id]['coins'].items():
      msg.append(f"{key}: {value}개")

  return "\n".join(msg)

def accountNum(id, today, args):
  return f"계좌번호: {id.decode('utf-8')}"

def sendMoney(id, today, args):
  otherId, amt = args
  otherId = bytes(otherId, encoding='utf-8')
  if otherId in db.keys():
    amt = int(amt)
    if db[id]['money'] >= amt:
      if amt <= 0:
        return "미쳤나 휴먼"
      db[id]['money'] -= amt
      db[otherId]['money'] += amt
      db[id] = db[id]
      db[otherId] = db[otherId]
      return "송금됐다 휴먼"
    else:
      return "너 거지다 휴먼"
  else:
    return "계좌번호 확인해라 휴먼"

def bankruptcycall(id, today, args):
  if 'bankrupt' not in db.keys():
    db['bankrupt'] = {}

  db['bankrupt'][id.decode('utf-8')] = True
  db['bankrupt'] = db['bankrupt']

  return "파산신청 됐다 휴먼"

