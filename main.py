import sys
sys.stdout.flush()
print("실행되니?")

import discord
from Database import db
import datetime
from TradingBot import TradingBot

class MyClient(discord.Client):
  bot = TradingBot()

  # override
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # override
  async def on_message(self, message):
    if message.author == client.user:
      return

    if message.content[0] != '/':
      return

    today = datetime.datetime.today()
    today = f"{today.year}-{today.month}-{today.day}"
    id = bytes(str(message.author.id), encoding='utf-8')
    
    if message.content == '/파산신청':
      if id in db.keys():
        del db[id]
        await message.channel.send("파산됐다 휴먼")
    else:
      msg = message.content.split()
      result = self.bot.handleMessage(msg[0][1:], id, today, msg[1:], message.author)
      await message.channel.send(result)


client = MyClient()
client.run('your key')
