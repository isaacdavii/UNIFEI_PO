from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco 
        self.__idade = idade
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome
    def getEndereco(self):
        return self.__endereco
    def getCpf(self):
        return self.__cpf
    def getIdade(self):
        return self.__idade
    
    @property
    def nome(self):
        return self.__nome
    @property
    def endereco(self):
        return self.__endereco
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao(self):
        pass
    
class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
        
    @property
    def titulacao(self):
        return self.__titulacao
    
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print(f"Professor {self.nome}, Titulação: {self.titulacao}, Endereço: {self.endereco}, Idade: {self.idade}, CPF: {self.cpf}")
        
class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso
        
    @property
    def curso(self):
        return self.__curso
    
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print(f"Aluno {self.nome}, Curso: {self.curso}, Endereço: {self.endereco}, Idade: {self.idade}, CPF: {self.cpf}")

class IdadeInvalida(Exception):
    pass

class TitulacaoInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CPFDuplicado(Exception):
    pass

if __name__ == "__main__":
    cadastros = {}
    
    listaExemplo = [
        ('São João Apóstolo', 'Rua A, 123', 40, '12345678901', 'Mestre'), # titulação inválida
        ('Maria Santíssima', 'Rua B, 456', 35, '23456789012', 'Doutor'), # OK
        ('São Pedro', 'Rua C, 789', 30, '34567890123', 'Doutor'), # OK
        ('João Paulo II', 'Rua D, 101', 28, '45678901234', 'Graduado'), # idade inválida
        ('Paulo VI', 'Rua D, 101', 50, '45678901234', 'Doutor'), # OK
        ('Francisco', 'Rua E, 202', 45, '78901234567', 'CCO'), # OK
        ('Leão XIV', 'Rua F, 303', 17, '67890123456', 'CCO'), # idade inválida
        ('Bento XVI', 'Rua G, 404', 22, '78901234567', 'SIN'), # já tem aluno com esse CPF
        ('João XXIII', 'Rua H, 505', 19, '89012345678', 'ECO'), # curso inválido
        ('São Lino', 'Rua I, 606', 25, '23456789012', 'SIN'), # já tem prof com esse CPF
        ('Pio XII', 'Rua J, 707', 20, '34567890124', 'CCO') # OK
    ]
    
    for nome, endereco, idade, cpf, titulacao in listaExemplo:
        try:
            if titulacao in ['Doutor', 'Mestre', 'Graduado']:
                # Cadastro de Professores
                if idade < 30 and idade >= 0:
                    raise IdadeInvalida("Idade menor que 30: " + str(idade))
                if titulacao not in ['Doutor']:
                    raise TitulacaoInvalida("Titulação inválida: " + titulacao)
                if cpf in cadastros:
                    raise CPFDuplicado("CPF já cadastrado: " + cpf)
               
                professor = Professor(nome, endereco, idade, cpf, titulacao)
                cadastros[cpf] = professor
                # Armazeno pelo CPF assim posso acessar alunos e professores pelo CPF e verificar duplicidade
                professor.printDescricao()
           
            elif titulacao in ['CCO', 'SIN', 'ECO']:
                # Cadastro de Alunos
                if idade < 18 and idade >= 0:
                    raise IdadeInvalida("Idade menor que 18: " + str(idade))
                if titulacao not in ['CCO', 'SIN']:
                    raise CursoInvalido("Curso inválido: " + titulacao)
                if cpf in cadastros:
                    raise CPFDuplicado("CPF já cadastrado: " + cpf)
                
                aluno = Aluno(nome, endereco, idade, cpf, titulacao)
                cadastros[cpf] = aluno       
                aluno.printDescricao()
        
        except (CPFDuplicado, IdadeInvalida, TitulacaoInvalida, CursoInvalido) as e:
            print(f'Erro ao cadastrar {nome}: {e}')