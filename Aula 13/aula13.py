from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome, pontoMensalFunc = None):
        self._codigo = codigo
        self._nome = nome
        self._pontoMensalFunc = pontoMensalFunc if pontoMensalFunc else []
        
    @property
    def codigo(self):
        return self._codigo
    @property
    def nome(self):
        return self._nome
    @property
    def pontoMensalFunc(self):
        return self._pontoMensalFunc
    
    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass
    
    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaFaltas(faltas)
                break
        
    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaAtrasos(atrasos)
                break
        
    def adicionaPonto(self, mes, ano, nroFaltas = 0, nroAtrasos = 0):
        ponto = PontoFunc(mes, ano, nroFaltas, nroAtrasos)
        self._pontoMensalFunc.append(ponto)
    
    def imprimeFolha(self, mes, ano):
        print(f'Código: {self._codigo}')
        print(f'Nome: {self._nome}')
        print(f'Salário Líquido: {self.calculaSalario(mes, ano):.2f}')
        print(f'Bônus: {self.calculaBonus(mes, ano):.2f}')
        
class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self._titulacao = titulacao
        self._salarioHora = salarioHora
        self._nroAulas = nroAulas
    
    @property
    def titulacao(self):
        return self._titulacao
    @property
    def salarioHora(self):
        return self._salarioHora
    @property
    def nroAulas(self):
        return self._nroAulas
    
    def calculaSalario(self, mes, ano):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroFaltas = ponto.nroFaltas
                salarioProf = self._salarioHora * self._nroAulas - self._salarioHora * nroFaltas
                return salarioProf
        return 0

    def calculaBonus(self, mes, ano):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroAtrasos = ponto.nroAtrasos
                salario = self.calculaSalario(mes, ano)
                bonus = salario * 0.1 - (salario * 0.01 * nroAtrasos)
                return max(bonus, 0)
        return 0
        
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self._funcao = funcao
        self._salarioMensal = salarioMensal
        
    @property
    def funcao(self):
        return self._funcao
    @property
    def salarioMensal(self):
        return self._salarioMensal
    
    def calculaSalario(self, mes, ano):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroFaltas = ponto.nroFaltas
                salarioTec = self._salarioMensal - ((self._salarioMensal / 30) * nroFaltas)
                return salarioTec
        return 0

    def calculaBonus(self, mes, ano):
        for ponto in self._pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                nroAtrasos = ponto.nroAtrasos
                salario = self.calculaSalario(mes, ano)
                bonus = salario * (0.08 - (0.01 * nroAtrasos))
                return max(bonus, 0)
        return 0

class PontoFunc():
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self._mes = mes
        self._ano = ano
        self._nroFaltas = nroFaltas
        self._nroAtrasos = nroAtrasos
        
    @property
    def mes(self):
        return self._mes
    @property
    def ano(self):
        return self._ano
    @property
    def nroFaltas(self):
        return self._nroFaltas
    @property
    def nroAtrasos(self):
        return self._nroAtrasos
    
    def lancaFaltas(self, nroFaltas):
        self._nroFaltas += nroFaltas
        
    def lancaAtrasos(self, nroAtrasos):
        self._nroAtrasos += nroAtrasos

if __name__ == "__main__":
    funcionarios = []
    
    prof = Professor(1, "João", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3_600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()