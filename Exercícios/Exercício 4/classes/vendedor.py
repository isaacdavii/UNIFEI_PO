from abc import ABC, abstractmethod
from classes.venda import Venda

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