#Bibliotecas usadas
from rich import print
from rich.table import Table
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import pyfiglet
from datetime import datetime

bot = ChatBot('Chat Botizinho')

#Perguntas e respostas
conversa = ['Oi', 'Olá!', 'O que precisa?'
            'Bom dia!','Bom dia, como posso ajudar?',
            'Como vai?', 'Estou bem, e você?',
            'Tudo Bem?','Tudo ótimo',
            'você foi programado na onde?', 'Fui programado em python',
            'Quem te criou?', 'Meu criador se chama Fernando, ele é genial :)',
            'me fale a hora'
            ]

#para que o bot memorize
treino = ListTrainer(bot)
treino.train(conversa)

#Estrutura do chatbot
os.system('cls')
print(Table(pyfiglet.figlet_format("Botizinho")))
print("Converse qualquer coisa com o botizinho ;)")
print("Para sair é só digitar: 'sair' ")

while True:
    #perguntas do usuario
    pergunta = input(">> ")
    if pergunta.lower() == "sair":
        print('Botizinho: Até Logo!')
        break
    elif pergunta.lower() == "hora":
        print("Botizinho:", datetime.now().strftime("%H:%M"))
        continue
    elif pergunta.startswith("calcule "):
        conta = pergunta.replace("calcule ", "")
        try:
            resultado = eval(conta)
            print("Botizinho: ", resultado)
        except:
            print("Botizinho: Conta inválida.")
        continue

    #respostas do chat
    resposta = bot.get_response(pergunta)

    if float(resposta.confidence) > 0.5:
        print('Botizinho:', resposta)
    else:
        print('Botizinho: Ainda não sei responder esta pergunta.')
        nova = input("Qual seria a resposta? ")
        
        treino.train([pergunta,nova])
        print("Botizinho: Aprendi algo novooo!")