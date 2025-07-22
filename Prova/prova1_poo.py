from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, cpf, nome, fone):
        self.__cpf = cpf
        self.__nome = nome
        self.__fone = fone

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, fone, salario, funcao):
        super().__init__(cpf, nome, fone)
        self.__salario = salario
        self.__funcao = funcao

    @property
    def salario(self):
        return self.__salario

    @property
    def funcao(self):
        return self.__funcao

class Cliente(Pessoa):
    def __init__(self, cpf, nome, fone, tipoCliente):
        super().__init__(cpf, nome, fone)
        self.__tipoCliente = tipoCliente
        self.__veiculos = []

    @property
    def tipoCliente(self):
        return self.__tipoCliente

    @property
    def veiculos(self):
        return self.__veiculos

    def addVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            self.veiculos.append(veiculo)

class Veiculo:
    def __init__(self, placa, marca, modelo):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo

    @property
    def placa(self):
        return self.__placa

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

class OrdemServico:
    def __init__(self, cliente, veiculo, funcionario, numeroOS, data):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__funcionario = funcionario
        self.__numeroOS = numeroOS
        self.__data = data
        self.__servicos = []

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def numeroOS(self):
        return self.__numeroOS

    @property
    def data(self):
        return self.__data

    @property
    def servicos(self):
        return self.__servicos

    def addServico(self, servico):
        if isinstance(servico, Servico):
            self.__servicos.append(servico)

    def imprimeOS(self):
        print(f"Número OS: {self.numeroOS}")
        print(f"Data: {self.data}")
        print(f"Placa do veículo: {self.veiculo.placa}")
        print(f"Nome proprietário: {self.cliente.nome}")
        print(f"Func responsável: {self.funcionario.nome}")
        print("-" * 43)
        print(f"{"Cod. Serviço":<20}{"Descrição"}")
        for servico in self.servicos:
            print(f"{servico.codigo:<20}{servico.descricao}")
        print("-" * 43)

class Servico:
    def __init__(self, codServico, descricao, valor):
        self.__codServico = codServico
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codServico

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

if __name__ == "__main__":
    func = Funcionario("999888776", "Luis Silva", "98877665", 1_800, "Atendente")
    cliente = Cliente("888777665", "João Souza", "9778855", "Vip")
    veiculo = Veiculo("PKO1234", "Chevrolet", "Onix")
    cliente.addVeiculo(veiculo)

    serv1 = Servico(100, "Alinhamento direção", 70)
    serv2 = Servico(101, "Balanceamento de rodas", 80)
    serv3 = Servico(102, "Troca de óleo", 120)

    os = OrdemServico(cliente, veiculo, func, 1001, datetime.now())
    os.addServico(serv1)
    os.addServico(serv2)
    os.addServico(serv3)
    os.imprimeOS()
