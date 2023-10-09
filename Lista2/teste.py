import random
aux = 0
tentativas = 0
aux2 = 0
lista = []



palavras = ['Python', 'Vasco', 'Guitarra', 'Batman', 'Azulejo', 'Basquete']
escolha = random.randint(0, 5)

adivinhar = palavras[escolha]
print(adivinhar)

for i in adivinhar:
    lista.append(i)
    aux += 1
    print(aux)

print(lista)

while tentativas < 6:

    print("vamu fase u bunecu amaratu") #fazer depois a forca
    print('_ ' * aux)

    palpite = input('Digite uma letra como palpite: ')

    verificacao = list(filter(lambda x: x in adivinhar, palpite))

    print(verificacao)
    if verificacao == []:
        print(False)
        tentativas += 1
    else:
        print(True)
        for i in adivinhar:
            if i != palpite:
                aux2 += 1
            else:
                conta = aux - aux2
                conta2 = aux - conta
                conta3 = aux - conta2
                print('_ ' * conta2, palpite, '_ ' * conta3)