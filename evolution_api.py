import requests

class EvolutionAPI:
    def __init__(self, url):
        self.url = url.rstrip("/")

    def enviar_mensagem(self, instance, apikey, sender_number, message):
        url = f"{self.url}/message/sendText/{instance}"
        payload = {
            "number": sender_number,
            "text": message,
            "delay": 2000
        }
        headers = {
            "apikey": apikey,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response.json()