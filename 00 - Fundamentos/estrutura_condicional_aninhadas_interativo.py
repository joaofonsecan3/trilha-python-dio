while True:  # Loop para manter o programa rodando até o usuário sair
    # Solicita ao usuário o tipo de conta
    tipo_conta = input("\nDigite o tipo de conta (normal, universitaria, especial): ").strip().lower()

    # Define saldo fixo para cada tipo de conta
    if tipo_conta == "normal":
        saldo = 2500
        cheque_especial = 450
    elif tipo_conta == "universitaria":
        saldo = 1000
        cheque_especial = 0
    elif tipo_conta == "especial":
        saldo = 10000
        cheque_especial = 0
    else:
        print("Tipo de conta inválido. Tente novamente.")
        continue  # Volta ao início do loop

    while True:  # Loop interno para permitir múltiplas operações
        # Solicita ao usuário a operação desejada
        operacao = input("\nDigite 'saldo' para consultar o saldo, 'saque' para realizar um saque ou 'sair' para encerrar: ").strip().lower()

        # Exibe o saldo disponível
        if operacao == "saldo":
            print(f"Seu saldo disponível é: R${saldo:.2f}")

        # Realiza o saque, se possível
        elif operacao == "saque":
            saque = float(input("Digite o valor do saque: "))

            if saldo >= saque:
                saldo -= saque
                print(f"Saque de R${saque:.2f} realizado com sucesso! Saldo restante: R${saldo:.2f}")
            elif tipo_conta == "normal" and saque <= (saldo + cheque_especial):
                saldo -= saque
                print(f"Saque de R${saque:.2f} realizado com uso do cheque especial! Saldo restante: R${saldo:.2f}")
            else:
                print("Saldo insuficiente!")

        elif operacao == "sair":
            print("Encerrando o programa...")
            exit()  # Encerra o script

        else:
            print("Operação inválida. Tente novamente.")