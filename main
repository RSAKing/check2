import re
import func

print ("////Bem Vindo ao RSA_Vazamentos\\\\")
print ("////Rannyere Andrade - RM 83387\\\\")

emails = {}

resp = "N"
while resp == "N":
    print("\nEscolha uma opção abaixo:\n")
    print("Insira 1 para Cadastrar um vazamento\n")
    print("Insira 2 para Listar vazamentos cadastrados\n")
    print("Insira 3 para Buscar um email (pelo ID)\n")
    print("Insira 4 para Sair\n")

    opcao = int(input("\nQual opção?\n"))
    if opcao == 1:
        func.cadastrar(emails)
    elif opcao == 2:
        func.exibir(emails)
    elif opcao == 3:
        func.buscar(emails)
    elif opcao == 4:
        resp = input("Deseja sair? S/N\n").upper()
    else:
        print("Invalido!")
        print("Try Again!")
