from classes.vendedor import Vendedor

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
