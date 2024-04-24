# Baralho Python POO ♠️🃏

Este projeto consiste na implementação de um baralho em Python utilizando programação orientada a objetos (POO). Ele inclui dois arquivos principais: `baralho.py` e `batalha.py`.

## Arquivo `baralho.py` 📂

Este arquivo contém a implementação das classes relacionadas ao baralho:

- **Classe `Naipe`:** Esta enumeração define os naipes das cartas: Ouros, Paus, Espadas e Copas.

- **Classe `Carta`:** Representa uma carta do baralho, contendo um número (valor) e um naipe. Ela possui métodos para retornar o valor e o naipe da carta como strings.

- **Classe `Baralho`:** Representa um conjunto de cartas. Cria um baralho completo com todas as cartas de cada naipe, embaralha o baralho e distribui as cartas entre os jogadores.

O programa principal no final do arquivo cria um baralho, o embaralha e distribui as cartas entre dois jogadores, exibindo as cartas de cada jogador.

## Arquivo `batalha.py` 🎲🥊

Este arquivo contém a implementação da lógica do jogo de batalha entre dois jogadores:

- **Classe `Batalha`:** Gerencia o jogo de batalha. O método `_iniciar_partida` inicializa o jogo, criando um baralho, embaralhando e distribuindo as cartas entre os jogadores. O método `jogar` realiza as rodadas do jogo, comparando as cartas dos jogadores e determinando o vencedor de cada rodada. O jogo continua até que todas as cartas de um jogador sejam utilizadas.

Para jogar, basta executar o arquivo `batalha.py` no terminal. Ele solicitará os nomes dos jogadores e iniciará a partida automaticamente.
