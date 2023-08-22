#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
#cada eleitor votar e ao final mostrar o número de votos de cada candidato

contador = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
eleitores = int(input('Quantos eleitores votarão nessa eleição?: '))
for contador in range(eleitores):
    votacao = int(input('Candidato 1 - Vote 1'
                        '\nCandidato 2 - Vote 2'
                        '\nCandidato 3 - Vote 3'
                        '\nVoto: '))
    if votacao == 1:
        candidato1 += 1
    if votacao == 2:
        candidato2 += 1
    if votacao == 3:
        candidato3 += 1
print(f'Candidato 1 recebeu {candidato1} votos')
print(f'Candidato 2 recebeu {candidato2} votos')
print(f'Candidato 3 recebeu {candidato3} votos')        
