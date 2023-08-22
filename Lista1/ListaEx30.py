#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99

verif = 'S'
compras = []
total = 0
produto = 1
posicao = 1

while verif == 'S':
    while produto != 0:
        produto = float(input('Preço do produto: '))
        if produto != 0:
            compras.append(produto)
        else:
            break
    print('-------------Lojas Mari_melhor_regencia------------------')
    for i in compras:
        print('Produto', posicao, ': ', compras[posicao - 1])
        posicao += 1
        total += i
    print(f'Valor total a pagar: R${total}')
    dinheiro = float(input('Dinheiro: '))
    print(f'Troco: R${dinheiro - total}')
    verif = input('S - Sim'
                '\nN - Não'
                '\nDeseja cadastrar mais compras?: ')
    if verif == 'S':
        compras.clear()
        total = 0
        produto = 1
        posicao = 1
