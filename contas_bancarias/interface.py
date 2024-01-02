from contas import Conta

while True:
    acao = input("\nAção (abrir/depositar/sacar/saldo/extrato/fechar/sair): ")

    if acao == "abrir":
        numero_conta = input("Número da conta: ")
        data_criacao = input("Data de criação da conta (DD/MM/AAAA): ")
        resultado = Conta.criar_conta(numero_conta, data_criacao)
        print(resultado)

    elif acao == "depositar":
        numero_conta = input("Número da conta: ")
        if numero_conta in Conta.contas:
            valor = float(input("Valor do depósito: "))
            data = input("Data (DD/MM/AAAA): ")
            conta_operacao = Conta.contas[numero_conta]
            resultado = conta_operacao.deposito(data, valor)
            print(resultado)
        else:
            print("Conta não encontrada")

    elif acao == "sacar":
        numero_conta = input("Número da conta: ")
        if numero_conta in Conta.contas:
            valor = float(input("Valor do saque: "))
            data = input("Data (DD/MM/AAAA): ")
            conta_operacao = Conta.contas[numero_conta]
            resultado = conta_operacao.saque(data, valor)
            print(resultado)
        else:
            print("Conta não encontrada")

    elif acao == "saldo":
        numero_conta = input("Número da conta: ")
        if numero_conta in Conta.contas:
            conta_operacao = Conta.contas[numero_conta]
            saldo = conta_operacao.saldo()
            print(f'Saldo atual: {saldo:.2f}')
        else:
            print("Conta não encontrada")

    elif acao == "extrato":
        numero_conta = input("Número da conta: ")
        data_inicio = input("Data de início do extrato (DD/MM/AAAA): ")
        if numero_conta in Conta.contas:
            conta_operacao = Conta.contas[numero_conta]
            conta_operacao.extrato(data_inicio)
        else:
            print("Conta não encontrada")

    elif acao == "fechar":
        numero_conta = input("Número da conta: ")
        if numero_conta in Conta.contas:
            conta_operacao = Conta.contas[numero_conta]
            resultado = conta_operacao.fechar_conta()
            print(resultado)
        else:
            print("Conta não encontrada")

    elif acao == "sair":
        print('Saindo do programa...')
        break

    else:
        print("Ação inválida")
