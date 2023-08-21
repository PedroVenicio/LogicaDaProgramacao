#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a 
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Largura da parede que será pintada: '))
altura = float(input('Altura da parede que será pintada: '))
area = altura * largura
print(f'Será necessário {area/2} litros de tinta para pintar a parede')
