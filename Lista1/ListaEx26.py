#Faça um programa que leia e valide as seguintes informações:

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('M - Masculino'
             '\nF - Feminino'
             '\nSexo: ')
civil = input('S - Solteiro'
              '\nC - Casado'
              '\nV - Viúvo'
              '\nD - Divorciado'
              '\nEstado civil: ')

verificar = len(nome)
if verificar < 3:
    print('Nome inválido: menor que 3 caracteres')
if idade < 0 or idade > 150:
    print('Idade inválida: deve ser entre 0 e 150')
if salario < 0:
    print('Salário inválido: deve ser maior que 0')

print(f'Nome: {nome}'
    f'\nIdade: {idade}'
    f'\nSalário: {salario}'
    f'\nSexo: {sexo}'
    f'\nEstado civil: {civil}')
