from datetime import *
import csv
from django.db.models import Count, Avg

from .lap import Lap, Mark

class Race:

    def __init__(self, path):
        self.arquivo = csv.reader(open(path), delimiter='\t',quotechar='|')
        self.result = list()

        next(self.arquivo, None) #Pula header do arquivo

        for row in self.arquivo:
            self.result.append(Lap(*row))

    def filtro(self,valor,lista):
        return filter(lambda x: x.piloto == valor,lista)

    def voltas(self):
        return self.result

    def classificacao(self):
        lista = list()
        # Trata Dados de cada piloto
        for i in self.result:
            if len(list(filter(lambda x: x.piloto == i.piloto,lista)))<=0:
                filtro = list(filter(lambda x: x.piloto == i.piloto,self.result))

                piloto = filtro[0].piloto
                voltas = len(filtro)
                hora_inicio = filtro[0].hora
                hora_fim = filtro[len(filtro)-1].hora
                tempo_total = datetime.combine(date.min,hora_fim()) - datetime.combine(date.min,hora_inicio())
                velocidade_media = sum(map(lambda x:x.velocidade_media,filtro))/len(filtro)

                melhor = sorted(filtro, key=lambda x:x.tempo_volta(), reverse=False)[0]
                melhor_tempo_volta = melhor.tempo_volta
                melhor_volta = melhor.volta

                mark = Mark(1,piloto,voltas,hora_inicio,hora_fim,tempo_total\
                            ,melhor_volta, melhor_tempo_volta,velocidade_media)
                lista.append(mark)

        lista = sorted(lista, key=lambda x:x.tempo_total, reverse=False)

        #Trata pilotos que não completaram a prova e seta tempos ###########################
        temp = list()
        for x in lista:
            if x.voltas<4:
                lista.remove(x)
                temp.append(x)
            else:
                x.tempo_apos_primeiro = str(x.tempo_total - lista[0].tempo_total)
                
        lista = lista + temp
        ######################## Trata posições ###############
        # print("Posicao | Piloto | Voltas | Tempo Total |  Melhor Volta|
        #  Melhor Tempo | Velocidade Media | Tempo apos primeiro  |")
        posicao = 0
        for mark in lista:
            posicao += 1
            mark.posicao = posicao

            # print(str(mark.posicao)+'  '+mark.piloto +"  |  "+str(mark.voltas)\
            # +" | "+str(mark.tempo_total)+" | "+str(mark.melhor_volta)\
            # +" | "+str(mark.melhor_tempo_volta())+" | "+str(mark.velocidade_media)\
            # +" | "+str(mark.tempo_apos_primeiro))

        return lista

    def tempo_total_prova(self):

        tempo_prova = datetime.combine(date.min,self.result[len(self.result)-1].hora())\
        - datetime.combine(date.min,self.result[0].hora())

        # print("Tempo Total "+str(tempo_prova))
        return str(tempo_prova)

    def melhor_volta(self):
        melhor_volta = sorted(self.result, key=lambda x:x.tempo_volta(), reverse=False)[0]

        # print("Melhor volta "+ str(melhor_volta.tempo_volta())+" | Piloto "+ melhor_volta.piloto)
        return melhor_volta
