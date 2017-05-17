from django.test import TestCase

from .race import Race
from .lap import Lap

class TestRace(TestCase):

    def setUp(self):
        self.tabela = []
        self.tabela.append(Lap('23:49:08.277','038 – F.MASSA',1,'1:02.852','44,275'))
        self.tabela.append(Lap('23:49:10.858','033 – R.BARRICHELLO',1,'1:04.352','43,243'))
        self.tabela.append(Lap('23:49:11.075','002 – K.RAIKKONEN',1,'1:04.108','43,408'))
        self.race = Race('/home/euclides/Desenv/dev-challenge/race.log')
    def testExist(self):
        self.result = self.race.voltas()
        self.assertEquals(len(self.result),23)
        self.assertEquals(self.result[0].hora(), self.tabela[0].hora())
        self.assertEquals(self.result[0].piloto, self.tabela[0].piloto)
        self.assertEquals(self.result[0].volta, self.tabela[0].volta)
        self.assertEquals(self.result[0].tempo_volta(), self.tabela[0].tempo_volta())
        self.assertEquals(self.result[0].velocidade_media, self.tabela[0].velocidade_media)

    def testeClassificacao(self):
        self.assertEquals(self.race.classificacao(),"")
