#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.

verif = True
while verif == True:
    valor = int(input('Digite um valor entre 0 e 10: '))
    if valor < 0 or valor > 10:
        print('Valor inválido')
        verif = True
    else:
        verif = False
