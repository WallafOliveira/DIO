depositos = []
saques = []

def Deposito():
    global valor
    deposito = float(input("Valor de Depósito: "))
    valor += deposito
    depositos.append(deposito)

def Saque():
    global valor
    saque = float(input("Valor de Saque: "))
    if saque <= valor:
        valor -= saque
        saques.append(saque)
    else:
        print("Saldo insuficiente para o saque.")

def Extrato():
    print("\n=========== Extrato ===========")
    print("Depósitos realizados:", depositos)
    print("Saques realizados:", saques)
    print(f"Saldo atual: R$ {valor:.2f}")
    print("===============================")

def CadastrarUsuario(usuarios):
    cpf = int(input("Digite seu CPF: "))
    usuario = filtrarusuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado.")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento})
    print("Usuário cadastrado com sucesso.")

def filtrarusuario(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None

def CriarConta(usuarios, listar_contas):
    cpf = int(input("Digite o CPF do titular da conta: "))
    usuario = filtrarusuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado.")
        return

    agencia = int(input("Digite o número da agência: "))
    valor_conta = float(input("Digite o valor inicial da conta: "))

    numero_conta = len(listar_contas) + 1

    conta = {
        "numero_conta": numero_conta,
        "agencia": agencia,
        "titular": usuario["nome"],
        "cpf_titular": cpf,
        "saldo": valor_conta
    }

    listar_contas.append(conta)
    print(f"\nConta criada com sucesso!\nNúmero da conta: {numero_conta}")

def Menu():
    print("""
======================= Menu =======================
[1] Para Depósito
[2] Para Saque
[3] Para Extrato
[4] Cadastrar novo Usuário
[5] Criar Conta
[6] Listar Contas
[7] Para Sair
====================================================
""")

def main():
    usuarios = []
    listar_contas = []
    valor = 0

    while True:
        Menu()
        acao = int(input("Escolha uma opção: "))

        if acao == 1:
            Deposito()
        elif acao == 2:
            Saque()
        elif acao == 3:
            Extrato()
        elif acao == 4:
            CadastrarUsuario(usuarios)
        elif acao == 5:
            CriarConta(usuarios, listar_contas)
        elif acao == 6:
            print("\n=========== Listagem de Contas ===========")
            for conta in listar_contas:
                print(f"Número da conta: {conta['numero_conta']}")
                print(f"Agência: {conta['agencia']}")
                print(f"Titular: {conta['titular']}")
                print(f"Saldo: R$ {conta['saldo']}")
                print("------------------------------------------")
            print("==========================================")
        elif acao == 7:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


main()
