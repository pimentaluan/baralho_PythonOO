from baralho import *
class Batalha:
    def __init__(self):
        self.__jogador1 = Jogador(input('Nome do jogador 1: ').title())
        self.__jogador2 = Jogador(input('Nome do jogador 2: ').title())
        
    def _iniciar_partida(self):
        baralho = Baralho()
        baralho.embaralhar()
        baralho.distribuir_cartas([self.__jogador1, self.__jogador2])
        
    def jogar(self):
        cartas_empate = []
        pontos_jogador1 = 0
        pontos_jogador2 = 0
        
        for rodada in range(50):
            try:
                carta_jogador1 = self.__jogador1.cartas.pop(0)
                carta_jogador2 = self.__jogador2.cartas.pop(0)
                
                if carta_jogador1._get_valor_como_string() > carta_jogador2._get_valor_como_string():
                    self.__jogador1.receber_cartas([carta_jogador2])
                    print(f'{self.__jogador1}: {carta_jogador1}x {self.__jogador2}: {carta_jogador2}')
                    print(f'{self.__jogador1} venceu a rodada {rodada+1} e adicionou {carta_jogador2} a sua pilha\n')
                    pontos_jogador1 += 1
                    if cartas_empate:
                        self.__jogador1.receber_cartas(cartas_empate)
                        print(f'E adicionou as cartas do empate a sua pilha: {cartas_empate}\n')
                        cartas_empate.clear()
                if carta_jogador1._get_valor_como_string() < carta_jogador2._get_valor_como_string():
                    self.__jogador2.receber_cartas([carta_jogador1])
                    print(f'{self.__jogador1}: {carta_jogador1}x {self.__jogador2}: {carta_jogador2}')
                    print(f'{self.__jogador2} venceu a rodada {rodada+1} e adicionou {carta_jogador1} a sua pilha\n')
                    pontos_jogador2 += 1
                    if cartas_empate:
                        self.__jogador1.receber_cartas(cartas_empate)
                        print(f'E adicionou as cartas do empate a sua pilha: {cartas_empate}\n')
                        cartas_empate.clear()
                if  carta_jogador1._get_valor_como_string() == carta_jogador2._get_valor_como_string():
                    print(f'{self.__jogador1}: {carta_jogador1}x {self.__jogador2}: {carta_jogador2}')
                    print(f'Empate na rodada {rodada+1} - Será necessário uma nova rodada\n')
                    cartas_empate.append(carta_jogador1)
                    cartas_empate.append(carta_jogador2)
            except IndexError:
                if pontos_jogador1 > pontos_jogador2: campeao = self.__jogador1 
                else: campeao = self.__jogador2
                
                print(f'Fim de jogo - O {campeao} foi o campeão')
                break
        
        
if __name__ == '__main__':
    batalha = Batalha()
    batalha._iniciar_partida()
    batalha.jogar()