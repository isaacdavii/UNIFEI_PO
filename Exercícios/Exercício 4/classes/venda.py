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
