from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self._nome = nome
        self._endereco = endereco
        self._idade = idade
        self._listaDisciplina = []
        
    @property
    def nome(self):
        return self._nome
    @property
    def endereco(self):
        return self._endereco
    @property
    def idade(self):
        return self._idade
    @property
    def listaDisciplina(self):
        return self._listaDisciplina
    
    # Método para inserir disciplina na lista de disciplinas
    def insereDisciplina(self, disciplina):
        self._listaDisciplina.append(disciplina)
    
    @abstractmethod
    def printDescricao(self):
        pass

class Disciplina():
    def __init__(self, nomeDisciplina, cargaHoraria):
        self._nomeDisciplina = nomeDisciplina
        self._cargaHoraria = cargaHoraria
        
    @property
    def nomeDisciplina(self):
        return self._nomeDisciplina
    @property
    def cargaHoraria(self):
        return self._cargaHoraria

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self._titulacao = titulacao
        
    @property
    def titulacao(self):
        return self._titulacao
    
    def printDescricao(self):
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Idade: {self.idade}')
        print(f'Titulação: {self.titulacao}')
        print('Disciplinas ministradas: ')
        for disciplina in self.listaDisciplina:
            print(f'Nome: {disciplina.nomeDisciplina} - Carga horária: {disciplina.cargaHoraria}')
        
class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self._curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    def printDescricao(self):
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Idade: {self.idade}')
        print(f'Curso: {self.curso}')
        print('Disciplinas cursadas: ')
        for disciplina in self.listaDisciplina:
            print(f'Nome: {disciplina.nomeDisciplina} - Carga horária: {disciplina.cargaHoraria}')

if __name__ == '__main__':
    # Criando instâncias de disciplinas
    disciplina1 = Disciplina('Matemática', 60)
    disciplina2 = Disciplina('Física', 45)
    disciplina3 = Disciplina('Química', 30)
    disciplina4 = Disciplina('Programação', 80)
    
    # Criando instâncias de professores e alunos
    professor1 = Professor('Carlos Silva', 'Rua A, 123', 40, 'Doutor')
    aluno1 = Aluno('Ana Souza', 'Rua B, 456', 20, 'Engenharia')
    
    # Inserindo disciplinas nos professores e alunos
    professor1.insereDisciplina(disciplina1)
    professor1.insereDisciplina(disciplina4)
    aluno1.insereDisciplina(disciplina2)
    aluno1.insereDisciplina(disciplina3)
    aluno1.insereDisciplina(disciplina4)
    
    # Imprimindo descrições
    print('Descrição do Professor:')
    professor1.printDescricao()
    
    print('\nDescrição do Aluno:')
    aluno1.printDescricao()
    