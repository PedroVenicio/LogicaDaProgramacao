#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.
temperatura = float(input('Qual a temperatura atual?: '))
if temperatura <=20:
    print('O ambiente está frio')
elif temperatura <= 26:
    print('O ambiente está agradável')
else: 
    print('O ambiente está calor')
