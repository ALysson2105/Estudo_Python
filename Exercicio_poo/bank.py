class ContaBancaria:
    def __init__(self,titular,numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0

    def dados_conta(self):
        dados = f"{self.titular}{self.numero_conta}{self.saldo}"
        print(dados)
        
    def deposito(self,valor):
        self.saldo += valor
        print(f"Este é seu novo saldo:{self.saldo}")
        
    def sacar(self,valor):
        
        if (self.saldo > valor):
            self.saldo -= valor
            print(f"Este é seu novo saldo:{self.saldo} ")
        else:
            print("Você não tem saldo suficiente para esta operação!")


cliente = ContaBancaria("Alysson", "1")

cliente.dados_conta()

cliente.deposito(50)

cliente.sacar(40)
        