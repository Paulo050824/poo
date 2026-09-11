class Contabancaria:
    def __init__(self,nome,saldo ):
        self.nome = nome
        self._saldo = saldo
    def __str__(self):
        return f"|Nome: {self.nome} \n|Saldo: {self.saldo} \n---------------------"
    def deposito(self, valor):
        self._saldo += valor
    def sacar(self, saque):
        if saque <= self._saldo:
            self._saldo -= saque
        else:
            print("Valor insuficiente!!")
    @property
    def saldo(self):
        return f"R${self._saldo}"



conta01 = Contabancaria("Claudio", 5800.00)
conta01.deposito(1500.00)
conta01.sacar(500.00)

conta02 = Contabancaria("Poliana", 12550.50)
conta02.deposito(25000.00)
conta02.sacar(10000.00)
print(conta01)
print(conta02)