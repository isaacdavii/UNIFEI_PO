class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self._marca = marca
        self._cor = cor
        self._motorLigado = motorLigado
        
    @property
    def marca(self):
        return self._marca
    @property
    def cor(self):
        return self._cor
    @property
    def motorLigado(self):
        return 'ON' if self._motorLigado else 'OFF'
    
    def ligar(self):
        if self._motorLigado == True:
            print('\nO motor já está ligado!')
        self._motorLigado = True     
              
    def desligar(self):
        if self._motorLigado == False:
            print('\nO motor já está desligado!')
        self._motorLigado = False
    
    # # método de instância
    # def ligaMotor(self):
    #     if self.__motorLigado == True:
    #         print('O motor já está ligado!')
    #     else:
    #         self.__motorLigado = True
    #         print('O motor acaba de ser ligado!')
    
class Carros(Veiculo):
    carros = []
    
    def __init__(self, marca, cor, motorLigado, portas, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self._portas = portas
        self._portaMalasCheio = portaMalasCheio
        Carros.carros.append(self)
        
    @property
    def portas(self):
        return self._portas
    
    @property
    def portaMalasCheio(self):
        return 'Cheio' if self._portaMalasCheio else 'Vazio'
    
    def verificarPortaMalas(self):
        if self._portaMalasCheio:
            print('O porta-malas está cheio!')
        else:
            print('O porta-malas está vazio!')
            
    def __str__(self):
        return f"{self.marca} | {self.cor} | {self.motorLigado} | {self.portas} | {self.portaMalasCheio}"    
    
    @classmethod
    def listar_carros(cls):
        print('--- LISTA DE CARROS ---')
        print(f"{'Marca'.ljust(15)} | {'Cor'.ljust(12)} | {'Ligado'.ljust(7)} | {'Portas'.ljust(7)} | {'Porta-malas'}")
        print('-' * 65)
        for carro in cls.carros:
            print(f"{carro.marca.ljust(15)} | {carro.cor.ljust(12)} | {carro.motorLigado.ljust(7)} | {str(carro.portas).ljust(7)} | {carro.portaMalasCheio}")
    
    
class Motos(Veiculo):
    motos = []
    
    # construtor
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado) 
        self._estilo = estilo
        Motos.motos.append(self)
        
    @property
    def estilo(self):
        return self._estilo
    
    def __str__(self):
        return f"{self.marca} | {self.cor} | {self.motorLigado} | {self.estilo}"
    
    @classmethod
    def listar_motos(cls):
        print('--- LISTA DE MOTOS ---')
        print(f"{'Marca'.ljust(15)} | {'Cor'.ljust(12)} | {'Ligado'.ljust(7)} | {'Estilo'}")
        print('-' * 51)
        for moto in cls.motos:
            print(f"{moto.marca.ljust(15)} | {moto.cor.ljust(12)} | {moto.motorLigado.ljust(7)} | {moto.estilo}")

    # # método de instância
    # def mostraAtributos(self):
    #     print('Esta motocicleta é uma {} {}'.format(self.__marca, self.__cor))
    #     if(self.__motorLigado):
    #         print('Seu motor está ligado')
    #     else:
    #         print('Seu motor está desligado')

# Instâncias
moto1 = Motos('Honda', 'vermelha', False, 'Naked')
moto2 = Motos('Yamaha', 'azul', True, 'Trail')
moto3 = Motos('Suzuki', 'preta', False, 'Custom')
moto4 = Motos('Kawasaki', 'verde', True, 'Sport')
moto5 = Motos('Ducati', 'branca', False, 'Cruiser')

carro1 = Carros('Fusca', 'azul', False, 4, False)
carro2 = Carros('Civic', 'preto', True, 4, True)
carro3 = Carros('Palio', 'branco', False, 4, False)
carro4 = Carros('Corsa', 'prata', True, 4, True)
carro5 = Carros('Gol', 'vermelho', False, 4, False)

Motos.listar_motos()
moto2.ligar()
moto1.desligar()
moto2.desligar()
Motos.listar_motos()
print()
# moto5.ligar()
# moto4.ligar()
# print()
# Motos.listar_motos()
# print()
# Carros.listar_carros()
# carro2.ligar()
# carro4.ligar()
# print()
# carro2.verificarPortaMalas()
# carro3.verificarPortaMalas()
# print()
Carros.listar_carros()
print()
print(moto1)
