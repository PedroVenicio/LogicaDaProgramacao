#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.

aux = 0
lista = []
verif = True
while verif == True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    if numero == 1000:
        break
for i in lista:
    aux = aux + i
print('Tamanho da lista: ', len(lista))
print(f'Soma de todos os números digitados: {aux - 1000}')
