import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)
data = response.json()

print("================================")
print("RESPOSTA DO TELEGRAM")
print("================================")
print(data)

if data.get("result"):
    for update in data["result"]:
        message = update.get("message")

        if message:
            chat = message.get("chat")

            if chat:
                print("================================")
                print("CHAT ID ENCONTRADO:")
                print(chat.get("id"))
                print("================================")
else:
    print("NENHUMA MENSAGEM ENCONTRADA")
