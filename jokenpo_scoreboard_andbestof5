import random
from time import sleep

print('- - ' * 12)
print('========== J O K E N P O   G A M E ============')
print('- - ' * 12)

print('''REGRAS DO JOGO:
Você deverá escolher apenas uma opção para jogar (Pedra, Papel ou Tesoura)
através do menu que irá aparecer. Pressione ENTER e boa sorte!
Tente me vencer se for capaz!
Faremos uma melhor de 5 jogadas, ok?''')

print('Vamos começar!')
nome_jog = str(input('Qual o seu nome? '))
print('Boa sorte, {}!'.format(nome_jog))
print('\n' * 2)

## Começo do jogo em rodadas
pl_jog = 0
pl_comp = 0

for n_aposta in range(1, 6):

    print('== {}º Rodada! =='.format(n_aposta))

    x = random.randint(1, 3) # Escolha computador
    y = int(input('''Escolha sua opção abaixo: 
    [ 1 ] Pedra (rock) 
    [ 2 ] Papel (paper) 
    [ 3 ] Tesoura (scissor) 
    Eu já escolhi a minha!
    Qual é a sua? =>  ''')) # Escolha jogador

    lista = ['Nada', 'Pedra', 'Papel', 'Tesoura']

    print('\n' * 1)
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('POO!!!')
    print('\n' * 1)

    if x == y:
        print('EMPATE!')
        print('Eu tb escolhi {}.'.format(lista[x]))
        print('Ninguém marcou ponto nesta jogada.')
    elif x == 1 and y == 2:
        print('Você GANHOU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
        pl_jog = pl_jog +1
    elif x == 1 and y == 3:
        print('Você PERDEU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
        pl_comp = pl_comp + 1
    elif x == 2 and y == 1:
        print('Você PERDEU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
        pl_comp = pl_comp + 1
    elif x == 2 and y == 3:
        print('Você GANHOU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
        pl_jog = pl_jog + 1
    elif x == 3 and y == 1:
        print('Você GANHOU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista [y]))
        pl_jog = pl_jog + 1
    elif x == 3 and y == 2:
        print('Você PERDEU!')
        print('Eu escolhi {} e você {}.'.format(lista[x], lista[y]))
        pl_comp = pl_comp + 1
    else:
        print('Você não escolheu nenhuma das opções entre 1 e 3. Tente novamente.')
        print('Está rodada foi perdida em nossa disputa...')

    if n_aposta < 5:
        print('\n' * 1)
        print('.....................................')
        print(' _____ PLACAR ATÉ A {}ª RODADA: _____'.format(n_aposta))
        print('.....................................')
        print('{}: {} ponto(s).'.format(nome_jog, pl_jog))
        print('Computador: {} ponto(s).'.format(pl_comp))
        print('\n' * 1)
        input('Aperte ENTER para continuar...')
    elif n_aposta == 5:
        print('\n' * 1)
        print(' --------- RESULTADO ---------')
        print('{}: {} ponto(s).'.format(nome_jog, pl_jog))
        print('Computador: {} ponto(s).'.format(pl_comp))
        print('--' * 16)
        print('\n' * 1)

    print('\n' * 4)  # Acrescenta 10 linhas para espaçar e ajudar no visual

if pl_jog > pl_comp:
    print('Parabéns, {}! Você VENCEU o desafio.'.format(nome_jog))
elif pl_jog < pl_comp:
    print('Você PERDEU, {}! Sou melhor que você.'.format(nome_jog))
else:
    print('Houve um EMPATE!')
print('FIM')
