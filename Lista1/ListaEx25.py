#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

verif = True
while verif == True:
    login = input('Digite o nome de usuário: ')
    senha = input('Digite sua senha: ')
    if login == senha:
        print('Erro: informações de login e senha iguais')
        verif = True
    else:
        print('Cadastro realizado com sucesso')
        verif = False
