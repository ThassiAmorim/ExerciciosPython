class ContaBancaria:

    def __init__ (self, nome, saldo_inicial = 0):
        self.nome = nome
        self.saldo = saldo_inicial
        print(f"\n------------------------------------------")
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito R${valor} realizado. Saldo atual: R${self.saldo}\n")

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            print(f"Saque no valor de R${valor} realizado. Saldo atual: R${self.saldo}\n")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo}\n")
    


if __name__ == "__main__":

    conta_Carlos = ContaBancaria("Carlos")

    conta_Carlos.depositar(20000)
    conta_Carlos.sacar(500)
    conta_Carlos.extrato()