#Bibliotecas usadas
from rich import print
from rich.table import Table
import pyfiglet
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

Responda a questão abaixo.

Este é um histórico da nossa conversa {context}

Pergunta: {question}

Resposta:
"""

bot = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | bot

def conversa_chat():
    context = ""
    print(Table(pyfiglet.figlet_format("Botizinho")))
    print("Converse qualquer coisa com o botizinho ;)")
    print("Para sair é só digitar: 'sair' ")

    while True:
        #perguntas do usuario
        pergunta = input(">> ")
        if pergunta.lower() == "sair":
            print('Botizinho: Até Logo!')
            break

        #respostas do chat
        resposta = chain.invoke({"context": "", "question": pergunta})
        print("Botizinho:", resposta)
        context += f"\nUser: {pergunta} \n AI:{resposta}"

if __name__ == "__main__":
    conversa_chat()
