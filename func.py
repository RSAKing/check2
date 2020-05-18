import re

def cadastrar(vazamento):
    check = "S"
    resp = "S"
    while resp == "S":
        tag = input("Informe o ID do vazamento >> ")
        while check == "S":
            email = input("Qual e-mail vazado?\n").upper()  
            if re.match("[^@]+@[^@]+\.[^@]+", email):
                check = "N"
            else:
                print("e-mail invalido informado")
                check = "S"
        check = "S"
        vazamento[tag] = [
            email,
            input("P4ssw0rd:\n"),
            ]
        resp = input("\nDeseja cadastrar mais? (S/N)\n").upper()

def exibir(vazamento):
    for tag, lista in vazamento.items():
            print("\nTag--->", tag)
            print("Email--->", lista[0])
            print("Senha--->", lista[1])

def buscar(vazamento):
    busca = input("Informe o ID do e-mail:\n")
    lista = vazamento.get(busca)
    if lista != None:
        print("\nEmail--->", lista[0])
        print("Senha--->", lista[1])
    else:
        print("Not Found!")