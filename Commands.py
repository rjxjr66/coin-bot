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

def manual(id, today, args):
  return """/출석: 출석합니다. 처음 사용시 반드시 출석해야 하며 하루에 한번 출석시 5000원을 드립니다.
/잔액: 잔액을 확인합니다.
/계좌번호: 자신의 계좌번호를 확인합니다.
/송금 [계좌번호] [금액(원화)]: [계좌번호]로 [금액]만큼 보냅니다.
/코인가격 [코인ID]: [코인ID]의 현재 가격을 확인합니다.
/매수 [코인ID] [금액(원화)]: [금액]만큼의 [코인ID]를 삽니다.
/매도 [코인ID] [개수]: [코인ID]코인을 [개수]만큼 팝니다.
/파산신청: 파산을 신청합니다."""

