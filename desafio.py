menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite uma opção: 
"""
# Variáveis para armazenar informações do usuário
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMTE_SAQUES = 3

# Menu
while True:

    opcao = int(input(menu))

    # Depósito
    if opcao == 1:
        valor_de_deposito = float(input("digite o valor que deseja depositar: "))

        if valor_de_deposito> 0:
            saldo+= valor_de_deposito
            print(f"Deposito realizado com sucesso! seu saldo atual é de R${saldo:.2f}")
            extrato += f"Depósito: R$ {valor_de_deposito:.2f}\n"
        else:
            print("Operação falhou! Digite um valor inteiro positivo para depositar!")

    # Saque
    elif opcao == 2:
        valor_de_saque = float(input("digite o valor que deseja sacar: "))
        if valor_de_saque > saldo:
            print("Saldo insuficiente")
        elif valor_de_saque > limite:
            print("O Valor máximo de saque é de R$500, por favor digite um valor menor")
        elif numero_de_saques >= LIMTE_SAQUES:
            print("O limite de saque diários é de 3 tentativas, por favor tente amanhã")
        elif valor_de_saque > 0:
            numero_de_saques += 1
            saldo -= valor_de_saque
            extrato += f"Saque: R$ {valor_de_saque:.2f}\n"
            print(f"Saque realizado com sucesso! seu saldo atual é de {saldo:.2f}")
        else:
            print("Operação falhou o valor informado é inválido")

    # Extrato
    elif opcao == 3:
        print("==== Extrato ====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    
    # Sair do sitema
    elif opcao == 0:
        print("Sistema finalizado")
        break
    
    else:
        print("opção inválida, por favor digite novamente a opção desejada")