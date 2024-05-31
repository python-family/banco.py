# Variáveis para controle de operações e saldo
depositos = []
saques = []
saldo = 0
saques_hoje = 0

# Função para realizar depósito
def depositar(valor):
    global saldo, depositos

    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito deve ser um valor positivo.")

# Função para realizar saque
def sacar(valor):
    global saldo, saques, saques_hoje

    if saques_hoje < 3 and valor <= 500 and valor <= saldo:
        saldo -= valor
        saques.append(valor)
        saques_hoje += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    elif saques_hoje >= 3:
        print("Limite de saques diários excedido.")
    elif valor > 500:
        print("Valor máximo de saque por operação é de R$ 500,00.")
    else:
        print("Saldo insuficiente para realizar o saque.")

# Função para exibir extrato
def exibir_extrato():
    global depositos, saques, saldo

    print("\nExtrato:")
    print("-" * 30)
    print("Depósitos:")
    for deposito in depositos:
        print(f"R$ {deposito:.2f}")
    print("Saques:")
    for saque in saques:
        print(f"R$ {-saque:.2f}")  # Saques são negativos no extrato
    print("-" * 30)
    print(f"Saldo atual: R$ {saldo:.2f}")

# Menu principal do sistema
while True:
    print("\nMenu Principal:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opção = int(input("Digite a opção desejada: "))

    if opção == 1:
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        depositar(valor_deposito)
    elif opção == 2:
        valor_saque = float(input("Digite o valor do saque: R$ "))
        sacar(valor_saque)
    elif opção == 3:
        exibir_extrato()
    elif opção == 4:
        print("Obrigado por utilizar o sistema bancário!")
        break
    else:
        print("Opção inválida. Tente novamente.")

