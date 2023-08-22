#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

contador = 1
fatorial = 1
valor = int(input('Digite um número inteiro para ser realizada a fatorial: '))
while contador <= valor:
    fatorial *= contador
    contador +=1
print(fatorial)
