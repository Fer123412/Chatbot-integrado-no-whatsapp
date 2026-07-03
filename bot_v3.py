#Bibliotecas usadas
import os
import flask
import requests
from dotenv import load_dotenv
from evolution_api import EvolutionAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

load_dotenv()

evolution = EvolutionAPI("http://localhost:8080")

instance = os.getenv("INSTANCE_NAME")
apikey = os.getenv("Evolution_API_KEY")
app = flask.Flask(__name__)

template = """

Responda a questão abaixo.

Este é um histórico da nossa conversa {context}

Pergunta: {question}

Resposta:
"""

bot = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | bot

@app.route("/webhook", methods=['POST'])
def webhook():

    print("Webkook chamado")
    data = flask.request.json
    print(data)

    pergunta = data.get("data", {}).get("message", {}).get("conversation")
    print("Pergunta:", pergunta)
    numero = (data.get("data", {}).get("key", {}).get("remoteJid", "").split("@")[0])

    if not pergunta:
        return flask.jsonify({"status":"Mensagem ignorada"})

    resposta = chain.invoke({
        "context": "",
        "question": pergunta
    })

    print("Respostas:", resposta)

    evolution.enviar_mensagem(
        instance = instance,
        apikey = apikey,
        sender_number = numero,
        message = resposta
    )

    print("=" * 50)
    print("CHEGOU REQUISIÇÃO")
    print(flask.request.method)

    if flask.request.method == "GET":
        return "Webhook OK"

    print(flask.request.json)

    return flask.jsonify({
        "status": "Mensagem enviada com sucesso"
    })
    
if __name__ == "__main__":
    app.run(port=5000)
