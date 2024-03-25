from random import shuffle
from enum import Enum

class Naipe(Enum):
    OUROS = 1
    PAUS = 2
    ESPADAS = 3
    COPAS = 4
class Carta:
    AS = 1
    VALETE = 11
    DAMA = 12
    REI = 13
    
    def __init__(self, numero, naipe: Naipe):
        self.__valor = numero
        self.__naipe = naipe
        

    def _get_valor_como_string(self):
        return self.__valor
    
    def _get_naipe_como_string(self):
        match self.__naipe:
            case Naipe.OUROS:
                return "Ouros"
            case Naipe.PAUS:
                return "Paus"
            case Naipe.ESPADAS:
                return "Espadas"
            case Naipe.COPAS:
                return "Copas"
        
    def __repr__(self) -> str:
        return f'Carta ({self._get_valor_como_string()} de {self._get_naipe_como_string()})'



class Baralho:
    def __init__(self):
        self.__cartas = []
        for naipe in Naipe:
            for numero in range(1, 14):
                self.__cartas.append(Carta(numero, naipe))
                
    @property
    def cartas(self):
        return self.__cartas

    def embaralhar(self):
        shuffle(self.__cartas)
        
    def __len__(self):
        return len(self.__cartas)

    def distribuir_cartas(self, jogadores: list):
        total_jogadores = len(jogadores)
        cartas_por_jogador = len(self.__cartas) // total_jogadores
        for i, jogador in enumerate(jogadores):
            inicio = i * cartas_por_jogador
            fim = inicio + cartas_por_jogador
            jogador.receber_cartas(self.__cartas[inicio: fim])
class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__cartas = []

    @property
    def cartas(self):
        return self.__cartas

    def receber_cartas(self, cartas: list[Carta]):
        self.__cartas.extend(cartas)

    def __repr__(self):
        return f'Jogador({self.__nome})'
    

if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()
    jogador1 = Jogador('Luan')
    jogador2 = Jogador('Luca')
    baralho.distribuir_cartas([jogador1, jogador2])
    print(jogador1.cartas)
    print(jogador2.cartas)