# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import credenciais
import funcoes

import pprint
import telepot

telegramBotToken = os.getenv('TELEGRAM_BOT_TOKEN')
telegram = telepot.Bot(telegramBotToken)

def processaResposta(textoDaMsg):

    if(textoDaMsg.find("/start")!=-1):
        return "Uau, você achou meu bot!"

    elif(textoDaMsg.find("/lançamentos")!=-1):
        return funcoes.lancamentos()

    elif(textoDaMsg.find("/similar")!=-1):
        busca = textoDaMsg.replace("/similar ","")
        return funcoes.similar(busca)

    else:
        return "Não conheço esse comando"


def recebendoMsg(msg):

    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    if(tipoChat=="group"):
        resposta = "Ainda não funciono para grupos. Me chama no privado ;)"
        telegram.sendMessage(chatID, resposta)

    else:

        if(tipoMsg=="text"):

            resposta = processaResposta(msg['text'])
            first_name = str(msg['chat']['first_name'])

            telegram.sendMessage(chatID, resposta)
            print("%s disse: \"%s\". Respondi com: \"%s\"" % (str(first_name), str(msg['text']), str(resposta)))


telegram.message_loop(recebendoMsg)

while True:
    pass
