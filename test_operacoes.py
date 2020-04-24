from unittest import TestCase
from com.jean.operacoes Import Opercoes

class TestOperacoes (TestCase):
  
   def setUp(self):
       self.operacoes = Operacoes()
       
       def test_soma(self):
           self.assertEqual(self.operacoes.soma([7, 2]), 9, "deveria ser 9")
