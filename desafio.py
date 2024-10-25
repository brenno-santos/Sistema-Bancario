menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Conta
[0] Sair

Digite uma opção: 
"""

def depositar(saldo, extrato, /):
    valor_de_deposito = float(input("digite o valor que deseja depositar: ")) 
    if valor_de_deposito > 0:
        saldo += valor_de_deposito
        print(f"Deposito realizado com sucesso! seu saldo atual é de R${saldo:.2f}")
        extrato += f"Depósito: R$ {valor_de_deposito:.2f}\n"
    else:
        print("Operação falhou! Digite um valor inteiro positivo para depositar!")
    
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_de_saques, limite_de_saques):
    valor_de_saque = float(input("digite o valor que deseja sacar: "))

    if valor_de_saque > saldo:
        print("Saldo insuficiente")
    elif valor_de_saque > limite:
        print("O Valor máximo de saque é de R$500, por favor digite um valor menor")
    elif numero_de_saques >= limite_de_saques:
            print("O limite de saque diários é de 3 tentativas, por favor tente amanhã")
    elif valor_de_saque > 0:
        numero_de_saques += 1
        saldo -= valor_de_saque
        extrato += f"Saque: R$ {valor_de_saque:.2f}\n"
        print(f"Saque realizado com sucesso! seu saldo atual é de R${saldo:.2f}")
    else:
        print("Operação falhou o valor informado é inválido")
        
    return saldo, extrato, numero_de_saques

def mostrar_extrato(saldo, extrato):
    print("==== Extrato ====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Seu saldo atual é de R$ {saldo:.2f}")

def criar_usuario(usuarios):

    cpf = input("Digite seu CPF(Somente números): ")

    if verificar_cpf(usuarios, cpf):
        print("cpf já cadastrado")
        return usuarios

    nome =  input("Digite seu nome completo: ")
    data = input("informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("infore o endereço(logradouro, numero - bairro - cidade/sigla estado): ")
    
    print("Usuário criado com sucesso!")
  
    usuarios.append({"cpf": cpf, "nome": nome, "data": data, "endereco": endereco})
    return usuarios

def verificar_cpf(usuarios,cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuarios

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Digite seu CPF: ")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado no sistema")
        return contas

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print("Conta criada com sucesso!")
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "nome": usuario_encontrado["nome"]})
        return contas
    else:
        print("Usuário não encontrado")
        return contas

def listar_contas(contas):
    if contas == []:
        print("Não há contas cadastradas no sistema")
    else:
        for conta in contas:
            print(f"""
====================================
    Agencia: {conta["agencia"]}
    N° Conta: {conta["numero_conta"]}
    Titular: {conta["nome"]}""")

def exibir_menu():
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    limite_de_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []
    numero_conta = 1
    
    while True:

        opcao = int(input(menu))
        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 2:
            saldo, extrato, numero_de_saques = sacar(
                saldo=saldo, 
                extrato=extrato, 
                limite=limite, 
                numero_de_saques=numero_de_saques,
                limite_de_saques=limite_de_saques
                )
        elif opcao == 3:
            mostrar_extrato(saldo,extrato)
        elif opcao == 4:
            usuarios = criar_usuario(usuarios)
        elif opcao == 5:
            contas = criar_conta(agencia, numero_conta, usuarios, contas)
            if contas:
                numero_conta = len(contas) + 1
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            print("Sistema finalizado")
            break
        else:
            print("opção inválida, por favor digite novamente a opção desejada")

exibir_menu()
