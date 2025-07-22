from classes.vendedor import Vendedor

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
