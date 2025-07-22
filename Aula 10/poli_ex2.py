from abc import ABC, abstractmethod

class Professor(ABC):
    professores = []
    
    def __init__(self, nome, matricula, cargaHoraria):
        self._nome = nome
        self._matricula = matricula
        self._cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self._nome
    @property
    def matricula(self):
        return self._matricula
    @property
    def cargaHoraria(self):
        return self._cargaHoraria

    @abstractmethod
    def calculaSalario(self):
        pass
    
    def calcularImposto(self, salarioBruto):
        # Método para calcular o imposto de renda
        if salarioBruto <= 1_903.98:
            return 0
        elif 1_903.99 <= salarioBruto <= 2_826.65:
            return 0.075 * salarioBruto 
        elif 2_826.66 <= salarioBruto <= 3_751.05:
            return 0.15 * salarioBruto
        elif 3_751.06 <= salarioBruto <= 4_664.68:
            return 0.225 * salarioBruto
        else:
            return 0.275 * salarioBruto
        # Retorna o valor do imposto de renda a ser descontado do salário bruto        

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter # setter para permitir alterar o valor do salário
    def salario(self, salario):
        self._salario = salario

    def calculaSalario(self):
        previdencia = 0.11 * self._salario
        imposto = self.calcularImposto(self._salario)
        return self._salario - (previdencia + imposto)

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self._salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self._salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self._salarioHora = salarioHora 

    def calculaSalario(self):
        imposto = self.calcularImposto(self._salarioHora * self.cargaHoraria)
        return self._salarioHora * self.cargaHoraria - imposto

if __name__ == "__main__":
    professor1 = ProfDE('Joao', 12_345, 40, 5_000)
    professor2 = ProfHorista('Paulo', 54_321, 30, 75)
    professor3 = ProfHorista('Ana', 56_789, 38, 95)
    
    professor1.salario = 6_000
    professor2.salarioHora = 85
    
    professores = [professor1, professor2, professor3]
    
    print('Lista de Professores:')
    print('---------------------')
    print(f"{'Nome'.ljust(15)} | {'Salário'}")   
    for professor in professores:
        print (f'{professor.nome.ljust(15)} | {professor.calculaSalario()}')

