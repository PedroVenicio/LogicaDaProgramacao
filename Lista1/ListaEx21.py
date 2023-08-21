#Crie um programa que leia dois valores e mostre na tela um menu

num1 = float(input('Digite o valor 1: '))
num2 = float(input('Digite o valor 2: '))
opcao = int(input('1 - Somar'
                '\n2 - Multiplicar'
                '\n3 - Maior'
                '\n4 - Menor'
                '\nEscolha a opção: '))
if opcao == 1:
    print(f'Soma dos valores: {num1 + num2}')
elif opcao == 2:
    print(f'Multiplicação dos valores: {num1 * num2}')
elif opcao == 3:
    print(f'Valor maior que (>): {num1 > num2}')
elif opcao == 4:
    print(f'Valor menor que (<): {num1 < num2}')
else:
    print('Opção inválida')
