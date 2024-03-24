from random import randint

class Cartas:
    __valor = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    __naipe = ['Copas', 'Espadas', 'Ouros', 'Paus']

    def __init__(self):
        self.__cartas = []
        self.gerar_cartas()

    @property
    def cartas(self):
        return self.__cartas

    def gerar_cartas(self):
        for valor in Cartas.__valor:
            for naipe in Cartas.__naipe:
                self.__cartas.append([valor, naipe])


class Baralho:
    def __init__(self):
        self.__cartas = Cartas().cartas

    def embaralhar(self):
        cartas_embaralhadas = []
        while len(self.__cartas) > 0:
            indice_carta = randint(0, len(self.__cartas) - 1)
            cartas_embaralhadas.append(self.__cartas.pop(indice_carta))
        self.__cartas = cartas_embaralhadas

    def distribuir_cartas(self, numero_jogadores):
        self.__mao = {}
        for i in range(numero_jogadores):
            self.__mao[f'Jogador {i+1}'] = []
        
        for i, carta in enumerate(self.__cartas):
            jogador_atual = i % numero_jogadores
            self.__mao[f'Jogador {jogador_atual+1}'].append(carta)
        
        return self.__mao

    
    def mao_jogador(self, jogador):
        return self.__mao[f'Jogador {jogador}']


if __name__ == '__main__':
    baralho = Baralho()
    baralho.embaralhar()
    baralho.distribuir_cartas(2)
    print(baralho.mao_jogador(1))
