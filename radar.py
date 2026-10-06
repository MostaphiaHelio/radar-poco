import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

mensagem = """🤖 RADAR POCO ONLINE!

✅ GitHub conectado
✅ Telegram conectado
✅ Sistema funcionando

Agora vamos começar a monitorar os preços dos POCOs. 📱🔥
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

dados = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

resposta = requests.post(url, json=dados)

print(resposta.json())
