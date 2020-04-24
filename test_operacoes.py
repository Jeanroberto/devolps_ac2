from unittest import TestCase
from com.jean.operacoes import Operacoes

class TestOperacoes(TesteCase):

    def setUp(self):
        Self.operacoes= Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([7, 2]),"Deveria ser 9")
