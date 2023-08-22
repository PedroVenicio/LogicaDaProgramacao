#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito

maindice=0
meindice= float('inf')
macidentes=''
meacidentes=''
totalveiculos=0
totalacidentes=0
cidademe2000=0
contador=1

for contador in range (5):
    cidade=(input('Nome da cidade: '))
    veiculos=int(input('Quantidade de veículos de passeio em 1999: '))
    acidentes=int(input('Quantidade de acidentes em 1999: '))
    if acidentes>maindice:
        maindice=acidentes
        macidentes=cidade
    if acidentes<meindice:
        meindice=acidentes
        meacidentes=cidade
    totalveiculos=totalveiculos+veiculos
    if veiculos<2000:
        totalacidentes=totalacidentes+acidentes
        cidademe2000=cidademe2000+1

print('----------------------Estatísticas---------------------------')
print(f'Cidade com mais acidentes: {macidentes}')
print(f'Total do maior indice: {maindice}')
print(f'Cidade com menos acidentes: {meacidentes}')
print(f'Total do menor indice: {meindice}')
mediaveiculos=totalveiculos/5
mediacidentes=totalacidentes/cidademe2000
print(f'Media de veiculos: {mediaveiculos}')
print(f'Media de acidentes em cidades com menos de 2000 veiculos: {mediacidentes}')
