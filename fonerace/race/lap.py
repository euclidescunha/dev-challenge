from datetime import *
import locale
_locale_radix = locale.localeconv()['decimal_point']

class Lap:
    hora = time(0, 0, 0, 0,)
    piloto = ''
    volta = 0
    tempo_volta = time(0, 0, 0, 0,)
    velocidade_media = 0.0
    def __init__(self, hora, piloto, volta, tempo_volta, velocidade_media):
        self.hora = datetime.strptime(hora,"%H:%M:%S.%f").time
        self.piloto = piloto
        self.volta = int(volta)
        self.tempo_volta = datetime.strptime(tempo_volta,"%M:%S.%f").time
        self.velocidade_media = locale.atof(velocidade_media.replace(",","."))

class Mark:
    posicao = 0
    piloto = ''
    voltas = 0
    hora_inicio = time(0, 0, 0, 0,)
    hora_fim = time(0, 0, 0, 0,)
    tempo_total = time(0, 0, 0, 0,)
    melhor_volta = 0
    melhor_tempo_volta = time(0, 0, 0, 0,)
    velocidade_media = 0.0
    tempo_apos_primeiro = time(0, 0, 0, 0,)

    def __init__(self, posicao, piloto, voltas,hora_inicio, hora_fim,\
                    tempo_total,melhor_volta ,melhor_tempo_volta, \
                    velocidade_media, tempo_apos_primeiro = time(0, 0, 0, 0,)):
        self.posicao = posicao
        self.piloto = piloto
        self.voltas = voltas
        self.tempo_total = tempo_total
        self.melhor_volta = melhor_volta
        self.melhor_tempo_volta = melhor_tempo_volta
        self.velocidade_media = velocidade_media
        self.tempo_apos_primeiro = tempo_apos_primeiro
