import csv

from .lap import Lap

class Race:

    def __init__(self, path):
        self.arquivo = csv.reader(open(path), delimiter='\t',quotechar='|')
        self.result = []
        self.classificacao = []
        next(self.arquivo, None) #Pula header do arquivo

        for row in self.arquivo:
            self.result.append(Lap(*row))

        # print(self.result[0].hora())
        # print(self.result[0].piloto)
        # print(self.result[0].volta)
        # print(self.result[0].tempo_volta())
        # print(self.result[0].velocidade_media)

    def voltas(self):
        return self.result

    def classificacao(self):

        return ""

    def tempo_total(self):

        return ""

    def melhor_volta(self):

        return ""
