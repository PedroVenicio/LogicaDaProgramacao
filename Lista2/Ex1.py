import random
aux = 0
tentativas = 0
tentativa = 0
lista = []
resposta = []

palavras = ['supino', 'python', 'vasco', 'guitarra', 'batman', 'azulejo', 'basquete']
escolha = random.randint(0, 5)

adivinhar = palavras[escolha]
print(adivinhar)

def verificacao(x):
    for i in lista:
        if i == palpite:
            posicao = lista.index(palpite)
            resposta[posicao] = palpite
            return resposta
        else:
            return x + 1


for i in adivinhar:
    lista.append(i)
    resposta.append('_')
    aux += 1


while tentativa < 6:

    print("vamu fase u bunecu amaratu") #fazer depois a forca

    palpite = input('Digite uma letra como palpite: ')

    tentativa = verificacao(tentativas)
    


        
