# Criação de game Snake & Ladders

import random as rd

# Número de jogos para avaliação de cenário
num_games = 10000

# Adicionando dicionários
snakes = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22}
ladders = {3: 16, 5: 7, 15: 25, 18: 20, 21: 32}

# Criação função do jogo


def game(snakes, ladders):
    posicao_inicial1 = 1
    posicao_inicial2 = 1

    while posicao_inicial1 < 36 and posicao_inicial2 < 36:
        dado1 = rd.randint(1, 6)
        nova_posicao1 = dado1 + posicao_inicial1
        if nova_posicao1 in snakes:
            posicao_inicial1 = snakes[nova_posicao1]
        elif nova_posicao1 in ladders:
            posicao_inicial1 = ladders[nova_posicao1]
        else:
            posicao_inicial1 = nova_posicao1

        dado2 = rd.randint(1, 6)
        nova_posicao2 = dado2 + posicao_inicial2
        if nova_posicao2 in snakes:
            posicao_inicial2 = snakes[nova_posicao2]
        elif nova_posicao2 in ladders:
            posicao_inicial2 = ladders[nova_posicao2]
        else:
            posicao_inicial2 = nova_posicao2

    return posicao_inicial1, posicao_inicial2


def simulacao(num_games):
    win1 = 0
    win2 = 0

    for i in range(num_games):

        posicao1, posicao2 = game(snakes, ladders)

        if posicao1 >= 36:
            win1 += 1
        elif posicao2 >= 36:
            win2 += 1

    return win1, win2


win1, win2 = simulacao(num_games)
print(win1, win2)



