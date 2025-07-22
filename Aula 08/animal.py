class Animal:
    #construtor
    def __init__(self,nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

    #metodo
    def fazerCarinho(self):
        print("{} está recebendo carinho".format(self.__nome))

class Gato(Animal):
    #construtor
    def __init__(self, nome, raca):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca

    #método
    def miar(self):
        print("Meow Meow")

class Cao(Animal):
    #construtor
    def __init__(self, nome):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)

    #método
    def latir(self):
        print("Au Au")     

if __name__ == "__main__":
    gato = Gato("Perola", "Siames")
    print(gato.nome)
    print(gato.raca)
    gato.miar()
    gato.fazerCarinho()
    cao = Cao("Cleitin")
    print(cao.nome)    
    cao.latir()    
    cao.fazerCarinho()