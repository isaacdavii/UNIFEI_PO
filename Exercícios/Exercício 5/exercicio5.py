from datetime import date
from abc import ABC

class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self._nroConta = nroConta
        self._nome = nome
        self._limite = limite
        self._senha = senha
        self._transacoes = []
        
    @property
    def nroConta(self):
        return self._nroConta
    @property
    def nome(self):
        return self._nome
    @property
    def limite(self):
        return self._limite
    @property
    def senha(self):
        return self._senha
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionaDeposito(self, valor, data, nomeDepositante):
        if valor > 0:
            self._transacoes.append(Deposito(valor, data, nomeDepositante))
            return True
        else:
            print('Valor inválido para depósito.')
            return False
        
    def adicionaSaque(self, valor, data, senha):
        if senha == self._senha:
            if valor > 0 and valor <= self.calculaSaldo():
                self._transacoes.append(Saque(valor, data, senha))
                return True
            else:
        #         print('Valor inválido para saque.')
                return False
        else:
        #     print('Senha incorreta.')
            return False
        
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha == self._senha:
            if valor > 0 and valor <= self.calculaSaldo():
                self.transacoes.append(Transferencia(valor, data, senha, "D"))
                contaFavorecido.transacoes.append(Transferencia(valor, data, senha, "C"))
                return True
            else:
        #         print('Valor inválido para transferência.')
                return False
        else:
        #     print('Senha incorreta.')
            return False
        
    def calculaSaldo(self):
        saldo = self._limite
        for transacao in self._transacoes:
            if isinstance(transacao, Deposito) or (isinstance(transacao, Transferencia) and transacao.tipoTransf == "C"):
                saldo += transacao.valor
            elif isinstance(transacao, Saque) or (isinstance(transacao, Transferencia) and transacao.tipoTransf == "D"):
                saldo -= transacao.valor
        return saldo
        

class Transacao(ABC):
    def __init__(self, valor, data):
        self._valor = valor
        self._data = data
    
    @property
    def valor(self):
        return self._valor
    @property
    def data(self):
        return self._data
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self._senha = senha
        
    @property
    def senha(self):
        return self._senha
    
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self._nomeDepositante = nomeDepositante
        
    @property
    def nomeDepositante(self):
        return self._nomeDepositante
    
    @nomeDepositante.setter
    def nomeDepositante(self, nomeDepositante):
        self._nomeDepositante = nomeDepositante
    
class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self._senha = senha
        self._tipoTransf = tipoTransf # 'D' para débito e 'C' para crédito
        
    @property
    def senha(self):
        return self._senha
    @property
    def tipoTransf(self):
        return self._tipoTransf


if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1_000, 'senha1')
    c1.adicionaDeposito(5_000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2_000, date.today(), 'senha1') is False:
        print('Não foi possível realizar o saque no valor de 2.000')
    if c1.adicionaSaque(1_000, date.today(), 'senha-errada') is False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1.000')
    
    c2 = Conta(4321, 'Joao de Souza', 1_000, 'senha2')
    c2.adicionaDeposito(3_000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1_500, date.today(), 'senha2') is False:
        print('Não foi possível realizar o saque no valor de 1.500')
    if c2.adicionaTransf(5_000, date.today(), 'senha2', c1) is False: # deve falhar
        print('Não foi possível realizar a transferência no valor de 5.000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) is False:
        print('Não foi possível realizar a transferência no valor de 800')
        
    print('--------')
    print(f'Saldo de c1: {c1.calculaSaldo()}') #deve imprimir 4_800
    print(f'Saldo de c2: {c2.calculaSaldo()}') #deve imprimir 1_700
