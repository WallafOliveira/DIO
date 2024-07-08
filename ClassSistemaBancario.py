from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = []
        self.bills = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def adicionar_bill(self, bill):
        self.bills.append(bill)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

class Bill:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

def Menu():
    print("""
======================= Menu =======================
[1] Para Depósito
[2] Para Saque
[3] Para Extrato
[4] Cadastrar novo Usuário
[5] Criar Conta
[6] Listar Contas
[7] Adicionar Conta a ser Paga
[8] Listar Contas a serem Pagas
[9] Para Sair
====================================================
""")

def main():
    usuarios = []
    listar_contas = []
    
    while True:
        Menu()
        acao = int(input("Escolha uma opção: "))

        if acao == 1:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                num_conta = int(input("Digite o número da conta: "))
                conta = buscar_conta(num_conta, usuario.contas)

                if conta:
                    valor = float(input("Valor de Depósito: "))
                    transacao = Deposito(valor)
                    usuario.realizar_transacao(conta, transacao)
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")

        elif acao == 2:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                num_conta = int(input("Digite o número da conta: "))
                conta = buscar_conta(num_conta, usuario.contas)

                if conta:
                    valor = float(input("Valor de Saque: "))
                    transacao = Saque(valor)
                    usuario.realizar_transacao(conta, transacao)
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")

        elif acao == 3:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                num_conta = int(input("Digite o número da conta: "))
                conta = buscar_conta(num_conta, usuario.contas)

                if conta:
                    print("\n=========== Extrato ===========")
                    for transacao in conta.historico.transacoes():
                        print(f"Tipo: {transacao['tipo']}, Valor: {transacao['valor']}")
                    print(f"Saldo atual: R$ {conta.saldo:.2f}")
                    print("===============================")
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")

        elif acao == 4:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                nome = input("Digite seu nome: ")
                data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
                usuarios.append(PessoaFisica(cpf, nome, data_nascimento, "Endereço fictício"))

                print("Usuário cadastrado com sucesso.")
            else:
                print("CPF já cadastrado.")

        elif acao == 5:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                agencia = int(input("Digite o número da agência: "))
                valor_conta = float(input("Digite o valor inicial da conta: "))

                conta = ContaCorrente(usuario, len(listar_contas) + 1)
                listar_contas.append(conta)

                usuario.adicionar_conta(conta)
                print(f"Conta criada com sucesso!\nNúmero da conta: {conta.numero}")

            else:
                print("Usuário não encontrado.")

        elif acao == 6:
            print("\n=========== Listagem de Contas ===========")
            for usuario in usuarios:
                print(f"CPF: {usuario._cpf}, Nome: {usuario._nome}")
                for conta in usuario.contas:
                    print(f"Número da conta: {conta.numero}")
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                    print("------------------------------------------")
            print("==========================================")

        elif acao == 7:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                descricao = input("Digite a descrição da conta a ser paga: ")
                valor = float(input("Digite o valor da conta a ser paga: "))

                bill = Bill(descricao, valor)
                usuario.adicionar_bill(bill)
                print("Conta a ser paga adicionada com sucesso.")

            else:
                print("Usuário não encontrado.")

        elif acao == 8:
            cpf = int(input("Digite seu CPF: "))
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                print("\n=========== Contas a serem Pagas ===========")
                for bill in usuario.bills:
                    print(f"Descrição: {bill.descricao}")
                    print(f"Valor: R$ {bill.valor:.2f}")
                    print("------------------------------------------")
                print("==========================================")
            else:
                print("Usuário não encontrado.")

        elif acao == 9:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if isinstance(usuario, PessoaFisica) and usuario._cpf == cpf:
            return usuario
    return None

def buscar_conta(numero_conta, contas):
    for conta in contas:
        if conta.numero == numero_conta:
            return conta
    return None

main()
