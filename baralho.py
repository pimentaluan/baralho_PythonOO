from random import randint

class Cartas:
    def __init__(self):
        self.__cartas = []
        self.__valor = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__naipe = ['Copas', 'Espadas', 'Ouros', 'Paus']

    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, novas_cartas):
        self.__cartas = novas_cartas

    def gerar_cartas(self):
        for valor in self.__valor:
            for naipe in self.__naipe:
                self.__cartas.append([valor, naipe])
    
class Baralho:
    def __init__(self):
        self.__cartas = Cartas()
        self.__cartas.gerar_cartas()
        
    def cartas_aleatorias(self):
        cartas_embaralhadas = []
        while len(self.__cartas.cartas) > 0:
            indice_carta = randint(0, len(self.__cartas.cartas) - 1)
            cartas_embaralhadas.append(self.__cartas.cartas.pop(indice_carta))
        self.__cartas.cartas = cartas_embaralhadas
    
    def distribuir_cartas(self, numero_jogadores):
        ... # Implementação do método distribuir_cartas
        
if __name__ == '__main__':
    baralho = Baralho()
    baralho.cartas_aleatorias()
    print(baralho.distribuir_cartas(4))