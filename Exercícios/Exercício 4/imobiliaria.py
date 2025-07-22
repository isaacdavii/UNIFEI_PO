from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self._codigo = codigo
        self._nome = nome
        self._vendas = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def vendas(self):
        return self._vendas

    def adicionaVenda(self, codImovel, mes, ano, valor):
        self.vendas.append(Venda(codImovel, mes, ano, valor))

    @abstractmethod
    def calculaRenda(self, mes, ano):  
        pass

    @abstractmethod
    def getDados(self):
        pass

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho):
        super().__init__(codigo, nome)
        self._nroCartTrabalho = nroCartTrabalho
        self._salarioFixo = salarioFixo
        
    @property
    def nroCartTrabalho(self):
        return self._nroCartTrabalho
    @property
    def salarioFixo(self):
        return self._salarioFixo

    def calculaRenda(self, mes, ano):
        totalVendas = sum((venda.valor * 0.01) for venda in self.vendas if venda.mes == mes and venda.ano == ano)
        return self._salarioFixo + totalVendas

    def getDados(self):
        return f"Nome: {self.nome} - Nro Carteira: {self.nroCartTrabalho}"

class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self._nroCPF = nroCPF
        self._comissao = comissao

    @property
    def nroCPF(self):
        return self._nroCPF

    @property
    def comissao(self):
        return self._comissao

    def calculaRenda(self, mes, ano):
        totalVendas = sum((venda.valor) for venda in self.vendas if venda.mes == mes and venda.ano == ano)
        return totalVendas * (self.comissao / 100)

    def getDados(self):
        return f"Nome: {self.nome} - Nro CPF: {self.nroCPF}"

class Venda:
    def __init__(self, codImovel, mes, ano, valor):
        self._codImovel = codImovel
        self._mes = mes
        self._ano = ano
        self._valor = valor
        
    @property
    def codImovel(self):
        return self._codImovel
    @property
    def mes(self):
        return self._mes
    @property
    def ano(self):
        return self._ano
    @property
    def valor(self):
        return self._valor

if __name__ == "__main__":
    funcContratado = Contratado(1001, "João da Silva", 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200_000)
    funcContratado.adicionaVenda(101, 3, 2022, 300_000)
    funcContratado.adicionaVenda(102, 4, 2022, 600_000)
    funcComissionado = Comissionado(1002, "José Santos", 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200_000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400_000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500_000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print(func.getDados())
        print("Renda no mês 3 de 2022: ")
        print(func.calculaRenda(3, 2022))