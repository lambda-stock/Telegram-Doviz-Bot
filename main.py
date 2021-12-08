# Kutuphaneleri import ediyoruz
import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os


#load_dotenv(".env", override=True)
bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Telegram sunucusuna bagliyoruz
app = Client(
    "LambdaBot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

# Json ile veri cekiyoruz
dovizjson = "https://finans.truncgil.com/today.json"
dovizcek = requests.get(dovizjson)
dovizveri = json.loads(dovizcek.text)

# Jsondan cekilen verileri degiskenlere atiyoruz
dolar = dovizveri["USD"]["Alış"]
euro = dovizveri["EUR"]["Alış"]
sterlin = dovizveri["GBP"]["Alış"]

# Baslat komutunda atilacak mesaji ayarliyoruz
@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""**Welcome** @{message.from_user.username}.
**Group**: ```{message.chat.title}```
**Invite Link**:  ```t.me/{message.chat.username}```
**Your User ID**: ```{message.from_user.id}```
You can contact with me from PM if you need more help.
""")

# Degiskenlere atadigimiz veriyi Telegram'a yukluyoruz
@app.on_message(filters.command("doviz"))
async def doviz(client, message):
    await client.send_message(message.chat.id, f"""
Dolar: ```{dolar}```
Euro: ```{euro}```
Sterlin: ```{sterlin}```
""")

app.run()
