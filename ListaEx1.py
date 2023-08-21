#Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
#pelo teclado e mostra na tela o seu tipo de dado.
print('---------------Some seus números----------------')
valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2 (que será somado): '))
soma = valor1 + valor2
print('Soma dos valores digitados: ', soma)
print('---------------Descubra o tipo do dado informado----------------')
a = input('Informe o dado: ')
print('O dado digitado é: ', type(a))
