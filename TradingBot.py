from Commands import attend, balance, accountNum, sendMoney, bankruptcycall
from coins import getPrice, buy, sell
from OpCommand import giveMoney, stealMoney, lockCoin, unlockCoin, bankruptcy, bankruptcylist

commands = {
  '출석': attend,
  '잔액': balance,
  '계좌번호': accountNum,
  '송금' : sendMoney,
  '코인가격': getPrice,
  '매수' : buy,
  '매도' : sell,
  '파산신청': bankruptcycall,
}

opCommands = {
  '입금': giveMoney,
  '출금': stealMoney,
  '잠금': lockCoin,
  '해금': unlockCoin,
  '파산':bankruptcy,
  '파산목록':bankruptcylist,
}

class TradingBot:
  def handleMessage(self, cmd, id, today, args, user):
    if cmd in commands:
      return commands[cmd](id, today, args)
    elif cmd in opCommands:
      if self.auth(user):
        return opCommands[cmd](id, today, args)
      else:
        return "너 따위가 쓸게 아니다 휴먼"
    else:
      return "잘못된 명령이다 휴먼"

  def auth(self, user):
    return len([ role for role in user.roles if role.name == "머스크" ]) > 0
