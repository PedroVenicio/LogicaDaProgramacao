#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.
print('=============Mercado compre bem==================')
produto = float(input('Valor do produto: '))
desconto = produto - (produto * 0.05)
aumento = produto + (produto * 0.15)
print(f'O produto com 5% de desconto será R${desconto} \nO produto com 15% de aumento será R${aumento}')
