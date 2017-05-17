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
