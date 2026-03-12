class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saque e depósitos.
    Essa conta bancaria precisa de um ‘ID’ e nome como obrigatório e o saldo é o opcional.
    Nessa classe tem métodos para depositar e sacar valores da conta bancaria
    """
    def __init__(self, id, nome, saldo=0): # Método Construtor
        # Atributos de Instância
        self.id = id
        self.titular = nome
        self.saldo = saldo

    # Métodos de Instância
    def __str__(self): # Dunder Attribute
        return  f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def depositar(self, valor):
        self.saldo += valor
        print(f'- Deposito de R${valor:,.2f} autorizado na conta {self.id}.')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo NEGADO de R${valor:,.2f} na conta {self.id}.\nSALDO INSUFICIENTE.')
        else:
            self.saldo -= valor
            print(f'- Saque de R${valor:,.2f} autorizado na conta {self.id}.')


# Main Program
conta1 = ContaBancaria(112, 'Gustavo', 3000)
conta1.depositar(500)
conta1.sacar(2_000_000)
print(conta1)
