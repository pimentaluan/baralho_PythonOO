from baralho import Baralho

class Batalha:
    def __init__(self, jogador1, jogador2):
        self.__baralho = Baralho()
        self.__jogador1 = []
        self.__jogador2 = []
        self.nome_jogador1 = jogador1
        self.nome_jogador2 = jogador2
        self.pontos_jogador1 = 0
        self.pontos_jogador2 = 0

    def puxar_carta(self):
        carta_jogador1 = self.__jogador1.pop(0)
        carta_jogador2 = self.__jogador2.pop(0)

        peso_jogador1 = self.peso_cartas.index(carta_jogador1[0])
        peso_jogador2 = self.peso_cartas.index(carta_jogador2[0])

        if peso_jogador1 == peso_jogador2:
            resultado = f'Empate - {self.nome_jogador1} venceu {self.pontos_jogador1} x {self.nome_jogador2} venceu {self.pontos_jogador2}'
        elif peso_jogador1 > peso_jogador2:
            self.pontos_jogador1 += 1
            resultado = f'{self.nome_jogador1} venceu {self.pontos_jogador1} x {self.nome_jogador2} venceu {self.pontos_jogador2}'
        else:
            self.pontos_jogador2 += 1
            resultado = f'{self.nome_jogador2} venceu {self.pontos_jogador2} x {self.nome_jogador1} venceu {self.pontos_jogador1}'

        return (f'{self.nome_jogador1}: {carta_jogador1}, {self.nome_jogador2}: {carta_jogador2}', resultado)

    def jogar(self):
        self.__baralho.embaralhar()
        self.__baralho.distribuir_cartas(2)
        self.__jogador1 = self.__baralho.mao_jogador(1)
        self.__jogador2 = self.__baralho.mao_jogador(2)
        self.peso_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        while self.__jogador1 and self.__jogador2:
            print(f"{self.nome_jogador1}: {len(self.__jogador1)} cartas, {self.nome_jogador2}: {len(self.__jogador2)} cartas")
            print(f"{self.nome_jogador1}: {self.__jogador1[0]}")
            print(f"{self.nome_jogador2}: {self.__jogador2[0]}")
            resultado = self.puxar_carta()
            print(f'{resultado[0]}')
            print(resultado[1])
            print()

        print(f"{self.nome_jogador1} venceu: {self.pontos_jogador1} x {self.nome_jogador2} venceu: {self.pontos_jogador2}")
        if self.pontos_jogador1 > self.pontos_jogador2:
            print(f"{self.nome_jogador1} é o campeão!")
        elif self.pontos_jogador1 < self.pontos_jogador2:
            print(f"{self.nome_jogador2} é o campeão!")
        else:
            print("Houve empate!")



if __name__ == '__main__':
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")

    batalha = Batalha(jogador1, jogador2)
    batalha.jogar()
