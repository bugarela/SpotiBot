# -*- coding: utf-8 -*-

padrao = "_{!s}_ - {!s}"
enumerado = "#{!s}: {!s}"

internacionais = "Últimos lançamentos internacionais:\n\n{!s}"
recomendacoes = "Recomendações para quem gosta de {!s}:\n\n{!s}"

erroPadrao = "Oops, algo deu errado :("
erroBusca = "Não encontrei musicas ou artistas parecidos com {!s} :("

def showInline(itens):
    last = (itens.pop(-1))['name']
    if not itens:
        return last
    init = ", ".join([item['name'] for item in itens])

    return " e ".join([init, last])

def showItem(item):
    return padrao.format(item['name'],showInline(item['artists']))

def showItensEnumerados(itens):
    return "\n\n".join([enumerado.format(i+1,showItem(item)) for i, item in enumerate(itens)])

def showItens(itens):
    return "\n\n".join([(showItem(item)) for item in itens])
