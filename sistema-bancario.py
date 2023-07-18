menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                saque = float(input("Informe o valor do saque: "))

                if saque <= limite and saque <= saldo and saque > 0:                  
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"\nSaque: R${saque:.2f}"
                else:
                        print("Valor de saque inválido.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Operação falhou! Limite de saques atingido.")

    elif opcao == "e":
            print("\n================Extrato================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: {saldo:.2f}")
            print("\n=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")