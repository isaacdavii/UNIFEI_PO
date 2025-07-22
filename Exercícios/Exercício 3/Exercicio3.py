from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    empregadas = []
    
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone
        
    @property
    def nome(self):
        return self._nome
    @property
    def telefone(self):
        return self._telefone
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
    
    @abstractmethod
    def getSalario(self):
        pass
    
    def maisBarata(self):
        # Método para encontrar a empregada mais barata
        
        menorSalario = float('inf') # Inicializa com infinito para garantir que qualquer salário será menor
        empregadaMaisBarata = None # Inicializa como None para garantir que sempre haverá uma empregada mais barata
        
        for empregada in empregadas:
            salario = empregada.getSalario()
            if salario < menorSalario:
                menorSalario = salario
                empregadaMaisBarata = empregada
        
        return empregadaMaisBarata
    
class EmpHorista(EmpDomestica):
    def __init__(self, nome, telefone, salarioHora, horasTrabalhadas):
        super().__init__(nome, telefone)
        self._salarioHora = salarioHora
        self._horasTrabalhadas = horasTrabalhadas
    
    # Em vez do nome "valorPorHora" alterei para "salarioHora" para melhor leitura e compreensão, assim vale também para "valorPorDia" e "valorMensal".
    @property
    def salarioHora(self):
        return self._salarioHora 
    @property
    def horasTrabalhadas(self):
        return self._horasTrabalhadas
    
    def getSalario(self):
        return self._salarioHora * self._horasTrabalhadas
    
class EmpDiarista(EmpDomestica):
    def __init__(self, nome, telefone, salarioDia, diasTrabalhados):
        super().__init__(nome, telefone)
        self._salarioDia = salarioDia
        self._diasTrabalhados = diasTrabalhados
        
    @property
    def salarioDia(self):
        return self._salarioDia
    @property
    def diasTrabalhados(self):
        return self._diasTrabalhados
    
    def getSalario(self):
        return self._salarioDia * self._diasTrabalhados
    
class EmpMensalista(EmpDomestica):
    def __init__(self, nome, telefone, salarioMes, mesesTrabalhados):
        super().__init__(nome, telefone)
        self._salarioMes = salarioMes
        self._mesesTrabalhados = mesesTrabalhados
    # Criei "mesesTrabalhados" apesar de não ser pedido para instanciar no exemplo para que fique mais claro o que é o salário mensal caso haja futuramente a necessidade de, por ex, explorar quanto a empregada receberia em 'n' meses.    
    
    @property
    def salarioMes(self):
        return self._salarioMes
    @property
    def mesesTrabalhados(self):
        return self._mesesTrabalhados
    
    def getSalario(self):
        return self._salarioMes * self._mesesTrabalhados
    
if __name__ == "__main__":
    # Instâncias de empregadas
    empregada1 = EmpHorista("Maria", "123456789", 12, 160)
    empregada2 = EmpDiarista("Ana", "987654321", 65, 20)
    empregada3 = EmpMensalista("Claudia", "456789123", 1_200, 1) #Explicação do porquê temos o valor '1' na class EmpMensalista
    
    empregadas = [empregada1, empregada2, empregada3]
    
    print('\n\033[7mLISTA DE EMPREGADAS\033[m')
    print('-' * len('LISTA DE EMPREGADAS'))
    print(f"{'Nome'.ljust(9)} | {'Telefone'.ljust(10)} | {'Salário'}")
    print('-' * 32)
    for empregada in empregadas:
        print(f"{empregada.nome.ljust(9)} | {empregada.telefone.ljust(10)} | {empregada.getSalario()}")
    
    empregadaMaisBarata = EmpDomestica.maisBarata(empregadas)
    print(f"""\nA empregada mais \033[1mbarata\033[m é:
Nome: {empregadaMaisBarata.nome} | Salário: {empregadaMaisBarata.getSalario()} | Telefone: {empregadaMaisBarata.telefone}""")
    
    
    
    # ATENÇÃO
    # Criei mais instâncias para testar a possibilidade de adicionar mais empregadas e verificar se o método "maisBarata" ainda funcionaria corretamente.
    empregada4 = EmpHorista("Juliana", "321654987", 15, 120)
    empregada5 = EmpDiarista("Fernanda", "654321789", 70, 15)
    empregada6 = EmpMensalista("Patricia", "789123456", 1_500, 2)
    
    empregadas.extend([empregada4, empregada5, empregada6]) # Adicionando novas empregadas à lista
    
    print('\n\n\033[7mLISTA DE EMPREGADAS ATUALIZADA\033[m')
    print('-' * len('LISTA DE EMPREGADAS ATUALIZADA'))
    print(f"{'Nome'.ljust(9)} | {'Telefone'.ljust(10)} | {'Salário'}")
    print('-' * 32)
    for empregada in empregadas:
        print(f"{empregada.nome.ljust(9)} | {empregada.telefone.ljust(10)} | {empregada.getSalario()}")
        
    empregadaMaisBarata = EmpDomestica.maisBarata(empregadas)
    print(f"""\nA empregada mais \033[1mbarata\033[m é:
Nome: {empregadaMaisBarata.nome} | Salário: {empregadaMaisBarata.getSalario()} | Telefone: {empregadaMaisBarata.telefone}""")


        
    