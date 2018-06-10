# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import funcoes

class TesteRespostasAPISpotify(unittest.TestCase):

    def test_lancamentos(self):
        tamanhoRetorno = len((funcoes.lancamentos()).split('\n'))
        self.assertEqual(tamanhoRetorno, 21, msg="Erro na funcao /lancamentos, tamanho:" + str(tamanhoRetorno))

    def test_similar(self):
        tamanhoRetorno = len((funcoes.similar("Test name")).split('\n'))
        self.assertEqual(tamanhoRetorno, 21, msg="Erro na funcao /similar, tamanho:" + str(tamanhoRetorno))

    def test_procuraArtista(self):
        self.assertNotEqual(funcoes.procuraArtista("The Beatles"),None)

    def test_procuraMusica(self):
        self.assertNotEqual(funcoes.procuraMusica("Let it Be"),None)

if __name__ == '__main__':
    unittest.main()
