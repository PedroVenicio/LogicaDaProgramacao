#Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos

nota1 = float(input('Nota da prova 1: '))
nota2 = float(input('Nota da prova 2: '))
nota3 = float(input('Nota da prova 3: '))
if nota1 > 5:
    print('Notas inválidas')
elif nota2 > 5:
    print('Notas inválidas')
elif nota3 > 10:
    print('Notas inválidas')
else:
    media = (nota1 + nota2 + nota3)/2
    if media < 6:
        print(f'Aluno reprovado \nMédia: {media}')
    else:
        print(f'Aluno aprovado \nMédia: {media}')
