#Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles.
lista = [4, 2, 12, 17, 22]
contador = 0
for i in lista:
    contador = contador + i
print(lista)
print(f'Soma dos números da lista: {contador}')
