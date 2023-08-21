#Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.
lista = ['Gabriel', 1.7, 10, 'Lucas', 'Paola']
for i in lista:
    if i == 10:
        print(lista.index(10))
