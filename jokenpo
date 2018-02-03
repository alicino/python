'''
Um programa que faça o computador jogar Jokenpô com você
Nível fácil (didático e básico)
PT-BR version
'''
import random

x = random.randint(1, 3) # Escolha computador
y = int(input('''Escolha sua opção abaixo: 
[ 1 ] Pedra (rock) 
[ 2 ] Papel (paper) 
[ 3 ] Tesoura (scissor) 
Eu já escolhi a minha! Qual é a sua? => ''')) # Escolha jogador

lista = ['Nada', 'Pedra', 'Papel', 'Tesoura']

if x == y:
    print('EMPATE!')
    print('Eu tb escolhi {}.'.format(lista[x]))
elif x == 1 and y == 2:
    print('Você GANHOU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
elif x == 1 and y == 3:
    print('Você PERDEU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
elif x == 2 and y == 1:
    print('Você PERDEU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
elif x == 2 and y == 3:
    print('Você GANHOU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
elif x == 3 and y == 1:
    print('Você GANHOU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista [y]))
elif x == 3 and y == 2:
    print('Você PERDEU!')
    print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
else:
    print('Você não escolheu nenhuma das opções entre 1 e 3. Tente novamente.')
