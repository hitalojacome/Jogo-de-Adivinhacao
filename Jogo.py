#Neste projeto usamos a função sleep da biblioteca time para dar um "suspense" quando o a máquina analisa a resposta do usiário.
#E também a função randint da biblioteca random para que o número secreto seja aleatório entre 1 e 20.

from time import sleep
from random import randint

#Introdução ao jogo, boas vindas, quantidade inicial de pontos.

pontos = 200
print('-=-'*15)
print('Bem vindo ao Jogo de Adivinhação em Python!')
print('\nVocê inicia com {} pontos.'.format(pontos))
print('-=-'*15)

num_secret = randint(1,20)
total_de_tentativas = 0

#Seleção de dificuldade de jogo, onde quanto mais difícil a dificuldade, menos chances de acertar o usuário terá.

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

#Se o usuário digitar um número menor que 1 ou maior que 20, ele irá receber um aviso de que está incorreto e perde uma rodada.

    if (num < 1 or num > 20):
        print("Você deve digitar um número entre 1 e 20!")
        continue

    acertou = num == num_secret
    maior   = num > num_secret
    menor   = num < num_secret

#Fim de jogo! Usando as estruturas condicionais finalizamos o jogo, se o usuário acertar ele sera parabenizado, mas se errar aparece no terminal se o chute dele foi maior ou menor que o numero secreto.

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

#Contagem de pontos finais.

        pontos_perdidos = abs(num_secret - num)
        pontos = pontos - pontos_perdidos
sleep(0.5)

print('Fim de jogo!')