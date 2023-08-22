#Faça um programa que jogue par ou impar com o computador. 

import random

repet = True
vitorias = 0
while repet == True:
    classe = int(input('1 - Par'
                    '\n2 - Ímpar'
                    '\nEscolha entre par ou ímpar: '))
    numerop = int(input('Digite um número de 1 a 5 para brincar de par ou ímpar: '))
    numerob = random.randint(1, 5)
    if classe == 1:
        if (numerob + numerop) % 2:
            print(f'Numero escolhido: {numerop}')
            print(f'Número do bot: {numerob}')
            print('Você perdeu')
            break
        else:
            print(f'Numero escolhido: {numerop}')
            print(f'Número do bot: {numerob}')
            print('Você venceu')
            vitorias += 1
    if classe == 2:
        if (numerob + numerop) % 2:
            print(f'Numero escolhido: {numerop}')
            print(f'Número do bot: {numerob}')
            print('Você venceu')
            vitorias += 1
        else:
            print(f'Numero escolhido: {numerop}')
            print(f'Número do bot: {numerob}')
            print('Você perdeu')
            break
print(f'Número de vitórias: {vitorias}')