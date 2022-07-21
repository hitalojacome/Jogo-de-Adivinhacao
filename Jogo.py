from time import sleep
from random import randint

pontos = 200

#Introdução ao jogo, boas vindas, quantidade inicial de pontos e
#opção de selecionar o nível que irá jogar.

print('-=-'*15)
print('Bem vindo ao Jogo de Adivinhação em Python!')
print('\nVocê inicia com {} pontos.'.format(pontos))
print('-=-'*15)

num_secret = randint(1,20)
total_de_tentativas = 0

print('(1) Fácil\n(2) Médio\n(3) Difícil')
nivel = int(input('Selecione a dificuldade: '))

if(nivel == 1 ):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 6
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print('Rodada {} de {}.'.format(rodada, total_de_tentativas))

    num = int(input('Digite um número entre 1 e 20: '))
    print('Analisando...')
    sleep(0.5)

    if (num < 1 or num > 20):
        print("Você deve digitar um número entre 1 e 20!")
        continue

    acertou = num == num_secret
    maior   = num > num_secret
    menor   = num < num_secret

    if (acertou):
        print('{} Parabéns! Você adivinhou o número!\nSua pontuação foi de {}.'.format(num_secret, pontos))
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior que o número secreto.')
            if (rodada == total_de_tentativas):
                print('O número secreto era {}.\nVocê fez {} pontos.'.format(num_secret, pontos))
        elif(menor):
            print('Você errou! O seu chute foi menor que o número secreto.')
            if (rodada == total_de_tentativas):
                print('O número secreto era {}.\nVocê fez {} pontos.'.format(num_secret, pontos))

        pontos_perdidos = abs(num_secret - num)
        pontos = pontos - pontos_perdidos
sleep(0.5)

print('Fim de jogo!')