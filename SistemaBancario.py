valor = 0
saque = 0
deposito = 0
depositos = []
saques = []


condicao = True


while(condicao):
    acao = int(input("""
--------------------------------------------------------------
                        [1] Para Deposito
                        [2] Para Saque
                        [3] Para Extrato
                        [4] Para Sair
------------------------------------------------------------
"""))
   
    if acao == 1:
        deposito = float(input("Valor de deposito: R$"))
        valor += deposito
        depositos.append(deposito)
    elif acao == 2:
        saque = float(input("Valor de saque: R$"))
        if saque <= valor:
            valor -= saque
            saques.append(saque)
        else:
            print("Saldo insuficiente")
    elif acao == 3:
        print("-------------EXTRATO--------------------")
        for i in range(len(depositos)):
          print("Deposito: R$",depositos[i])
        for i in range(len(saques)):
          print("Saque: R$",saques[i])
        print("Valor total: R$", valor)
    elif acao == 4:
        condicao = False
        print("""
        -------------EXTRATO FINAL--------------------

                    Valor total:R${}
        """ .format(valor))
    else:
        print("operação invalida")
    
