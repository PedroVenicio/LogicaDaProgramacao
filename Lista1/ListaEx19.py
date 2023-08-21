#Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 

opcao = int(input('1 - Soma de 2 números' 
                '\n2 - Diferença entre 2 números' 
                '\n3 - Produto entre 2 números'
                '\n4 - Divisão entre 2 números' 
                '\nEscolha a opção: '))
if opcao == 1:
    num1 = float(input('Digite o número 1: '))
    num2 = float(input('Digite o número 2: '))
    print(f'Soma dos números digitados: {num1 + num2}')
elif opcao == 2:
    num1 = float(input('Digite o número 1: '))
    num2 = float(input('Digite o número 2: '))
    print(f'Diferença entre os números digitados: {num1 - num2}')
elif opcao == 3:
    num1 = float(input('Digite o número 1: '))
    num2 = float(input('Digite o número 2: '))
    print(f'Produto entre os números digitados: {num1 * num2}')
elif opcao == 4:
    num1 = float(input('Digite o número 1: '))
    num2 = float(input('Digite o número 2: '))
    print(f'Divisão entre os números digitados: {num1 / num2}')
else:
    print('Opção inválida')
