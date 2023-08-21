#Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura): 
#Homens: (72.7 ∗ h) − 58
#Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input('Digite sua altura: '))
sexo = int(input('1 - Masculino \n2 - Feminino \nQual seu sexo?: '))
if sexo == 1:
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso}Kg')
if sexo == 2:
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso}Kg')
