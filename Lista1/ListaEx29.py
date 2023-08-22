#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.

tabela = []
aux = 0
for i in range(51):
    aux = aux + i
    valor = 1.99*i
    tabela.append( valor)
    print(i,'R$', tabela)
    tabela.clear()
