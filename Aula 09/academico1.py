from abc import ABC, abstractmethod
# Abstract Base Class (ABC) é uma classe que não pode ser instanciada diretamente.
# Ela serve como um modelo para outras classes, definindo métodos e propriedades que devem ser implementados nas subclasses.

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

    def insereDisciplina(self, disciplina):
        self._listaDisciplina.append(disciplina)

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self._titulacao = titulacao

    @property
    def titulacao(self):
        return self._titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Titulação: {}'.format(self.titulacao)) 
        print('Disciplinas ministradas: ')
        for disciplina in self.listaDisciplina:
            print('Nome: {} - Carga horária: {}'.format(disciplina.nomeDisciplina,
                                                        disciplina.cargaHoraria))     

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    def printDescricao(self):
        print('Nome: {}'.format(self.nome))
        print('Endereço: {}'.format(self.endereco))
        print('Idade: {}'.format(self.idade))
        print('Curso: {}'.format(self.curso))   
        print('Disciplinas cursadas: ')
        for disciplina in self.listaDisciplina:
            print('Nome: {} - Carga horária: {}'.format(disciplina.nomeDisciplina,
                                                        disciplina.cargaHoraria))              

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

if __name__ == "__main__":
    disciplina1 = Disciplina('Programacao OO', 64)
    disciplina2 = Disciplina('Estruturas de Dados', 64)
    disciplina3 = Disciplina('Banco de Dados', 64)

    prof = Professor('Joao','Av. BPS, 1303', 44, 'doutorado')
    prof.insereDisciplina(disciplina1)
    prof.insereDisciplina(disciplina2)
    prof.printDescricao()
    print()
    aluno = Aluno('Pedro','Av. Cesario Alvim, 205', 20, 'SIN')
    aluno.insereDisciplina(disciplina1)
    aluno.insereDisciplina(disciplina2)
    aluno.insereDisciplina(disciplina3)
    aluno.printDescricao()