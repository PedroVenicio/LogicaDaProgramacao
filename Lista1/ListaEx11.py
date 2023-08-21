#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.
nome = input('Nome do funcionário: ')
horast = int(input('Quantidade de horas trabalhadas: '))
vhora = float(input('Valor da hora: '))
salario = horast * vhora
desc = salario - salario*0.02
print(f'O funcionário {nome} receberá, com o desconto do INSS incluso, R${desc} por trabalhar por {horast} horas')
