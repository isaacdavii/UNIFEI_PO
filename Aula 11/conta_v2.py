from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nroConta, titular, saldo):
        self._nroConta = nroConta
        self._titular = titular
        self._saldo = saldo
        self._extrato = []
        
    @property
    def nroConta(self):
        return self._nroConta
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def extrato(self):
        return self._extrato
    
    @abstractmethod
    def deposito(self, valor, descricao):
        pass
    
    @abstractmethod
    def impExtrato(self):
        pass
    
    
class ContaCorrente(Conta):
    def __init__(self, nroConta, titular, saldo, mensalidade):
        super().__init__(nroConta, titular, saldo)
        self._mensalidade = mensalidade
        
    @property
    def mensalidade(self):
        return self._mensalidade
    
    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self._mensalidade = mensalidade
    
    def deposito(self, dia, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._extrato.append(f'Dia: {dia} - Depósito: {descricao} - R$ {valor:.2f}')
            return True
        else:
            print(f'Conta: {self._nroConta} - Depósito: {valor:.2f} - Valor de depósito inválido!\n')
            return False
    
    def saque(self, dia, valor, descricao):
        if valor > 0:
            if self._saldo + valor >= 0:
                self._saldo -= valor
                self._extrato.append(f'Dia: {dia} - Saque: {descricao} - R$ {valor:.2f}')
                return True
            else:
                print(f'Conta: {self._nroConta} - Saque: {valor:.2f} - Saldo insuficiente!\n')
                return False
        else:
            print(f'Conta: {self._nroConta} - Saque: {valor:.2f} - Valor de saque inválido!')
            return False
        
    def impExtrato(self):
        print(f'Extrato da conta {self._nroConta} - {self._titular}')
        print(f'Transações: {len(self._extrato)}')
        for transacao in self._extrato:
            print(transacao)
        print(f'Saldo atual: R$ {self._saldo:.2f}')
    
class ContaLimite(Conta):
    def __init__(self, nroConta, titular, saldo, limite):
        super().__init__(nroConta, titular, saldo)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, limite):
        self._limite = limite
    
    def deposito(self, dia, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._extrato.append(f'Dia: {dia} - Depósito: {descricao} - R$ {valor:.2f}')
            return True
        else:
            print(f'Conta: {self._nroConta} - Depósito: {valor:.2f} - Valor de depósito inválido!')
            return False
        
    def saque(self, dia, valor, descricao):
        if valor < self._saldo + self._limite:
            # Verifica se o saldo mais o valor do saque não ultrapassa o limite
            self._saldo -= valor
            self._extrato.append(f'Dia: {dia} - Saque: {descricao} - R$ {valor:.2f}')
            return True
        else:
            print(f'Conta: {self._nroConta} - Saque: {valor:.2f} Saldo insuficiente!\n')
            return False
    
    def impExtrato(self):
        print(f'Extrato da conta {self._nroConta} - {self._titular}')
        print(f'Transações: {len(self._extrato)}')
        for transacao in self._extrato:
            print(transacao)
        print(f'Limite: R$ {self._limite:.2f}')
        print(f'Saldo atual: R$ {self._saldo:.2f}')

class ContaPoupanca(Conta):
    def __init__(self, nroConta, titular, saldo, diaAniversario):
        super().__init__(nroConta, titular, saldo)
        self._diaAniversario = diaAniversario
        
    @property
    def taxaRendimento(self):
        return self._diaAniversario
    @taxaRendimento.setter
    def taxaRendimento(self, diaAniversario):
        self._diaAniversario = diaAniversario
        
    def deposito(self, dia, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._extrato.append(f'Dia: {dia} - Depósito: {descricao} - R$ {valor:.2f}')
            return True
        else:
            print(f'Conta: {self._nroConta} - Depósito: {valor:.2f} - Valor de depósito inválido!\n')
            return False
        
    def saque(self, dia, valor, descricao):
        if valor > 0:
            if self._saldo + valor >= 0:
                self._saldo -= valor
                self._extrato.append(f'Dia: {dia} - Saque: {descricao} - R$ {valor:.2f}')
                return True
            else:
                print(f'Conta: {self._nroConta} - Saque: {valor:.2f} - Saldo insuficiente!')
                return False
        else:
            print(f'Conta: {self._nroConta} - Saque: {valor:.2f} - Valor de saque inválido!')
            return False
    
    def impExtrato(self):
        print(f'Extrato da conta {self._nroConta} - {self._titular}')
        print(f'Transações: {len(self._extrato)}')
        for transacao in self._extrato:
            print(transacao)
        print(f'Dia do Aniversário do Rendimento: {self._diaAniversario}')
        print(f'Saldo atual: R$ {self._saldo:.2f}')


if __name__== "__main__":
    contas = []
    
    conta1 = ContaCorrente(1111, 'Matheus ', 5_200, 30)
    conta2 = ContaLimite(2222, 'Rodrigo', 3_000, 1_000)
    conta3 = ContaPoupanca(3333, 'Samuel', 10_000, 10)
    contas.append(conta1)
    contas.append(conta2)
    contas.append(conta3)
    
    conta1.deposito(4, 1_000, 'Crédito salário')
    conta1.deposito(5, -500, 'PIX')
    conta2.deposito(3, 1_500, 'Crédito salário')
    conta3.deposito(5, 1_200, 'Estágio')
    
    conta1.saque(11, 500, 'CEMIG')
    conta1.saque(12, 5_500, 'Luz')
    conta2.saque(12, 40_000, 'PIX')
    conta3.saque(10, 1_200, 'COPASA')
    
    conta1.saque(15, 400, 'Roupa')
    conta2.saque(20, 750, 'Academia')
    conta3.saque(25, 300, 'Tatuagem')
    conta3.saque(18, 500, 'Rolê inominável')

    for conta in contas:
        conta.impExtrato()
        print()