#Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:

idade = int(input('Digite sua idade: '))
tempo = int(input('Digite seu tempo de serviço: '))
if idade >= 65 or tempo >=30 or idade >= 60 and tempo >= 25:
    print('Você pode se aposentar')
else:
    print('Você não pode se aposentar')
