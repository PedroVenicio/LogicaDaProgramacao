#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
#valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
#não continuar a escrever valores.

menor = float('inf')
maior = 0
lista = []
aux = 0
repet = 'S'
while repet == 'S':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    repet = input('Continuar a digitar valores?: '
        '\nS - Sim'
        '\nN - Não'
        '\nEscolha sua opção: ')
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    if repet == 'N':
        break
for i in lista:
    total = len(lista)
    aux = aux + i
media = aux/total
print('Valores digitados: ', lista)
print(f'Média dos valores: {media}')
print(f'Maior valor lido: {maior}')
print(f'Menor valor lido: {menor}')
