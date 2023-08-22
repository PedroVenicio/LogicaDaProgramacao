#Em uma eleição presidencial existem quatro candidatos.

total = 0
total1=0
total2=0
total3=0
total4=0
totalnulo=0
totalbranco=0
contador=1
repet = 'S'

while repet == 'S':
    voto = int(input('Câmara de votos:'
                    '\n1 - Candidato 1'
                    '\n2 - Candidato 2'
                    '\n3 - Candidato 3'
                    '\n4 - Candidato 4'
                    '\n5 - Voto nulo'
                    '\n6 - Voto em branco'
                    '\n0 - Terminar os votos'
                    '\nInsira seu voto: '))
    total += 1
    if voto == 1:
        total1 += 1 
    if voto == 2:
        total2 += 1
    if voto == 3:
        total3 += 1
    if voto == 4:
        total4 += 1
    if voto == 5:
        totalnulo += 1
    if voto == 6:
        totalbranco += 1
    if voto == 0:
        total -= 1
        break

print('-------------------Resultados da eleição--------------------------')
print('Total de votos dos candidatos:')
print(f'Total de votos para Candidato 1: {total1}')
print(f'Total de votos para Candidato 2: {total2}')
print(f'Total de votos para Candidato 3: {total3}')
print(f'Total de votos para Candidato 4: {total4}')
print(f'Total de votos nulos: {totalnulo}')
print(f'Porcentagem de votos nulos: {(totalnulo/total) * 100}')
print(f'Total de votos em branco: {totalbranco}')
print(f'Porcentagem de votos nulos: {(totalbranco/total) * 100}')
