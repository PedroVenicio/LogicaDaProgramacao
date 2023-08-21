#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.
conversao = int(input('Você deseja converter: \n1 - Celsius pra Farenheit \n2 - Farenheit pra Celsius \nDigite sua escolha: '))
if conversao == 1:
    cel = float(input('Temperatura em graus Celsius: '))
    f = cel * 1.8 + 32
    print(f'Temperatura convertuda de Celsius para Farenheit: {f}')
if conversao == 2:
    far = float(input('Temperatura em graus Farenheit: '))
    c = (far - 32)/1.8
    print(f'Temperatura convertida de Farenheit para Celsius: {c}')
