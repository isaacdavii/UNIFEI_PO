from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._listaItens = []
        
    @property
    def numero(self):
        return self._numero
    @property
    def cliente(self):
        return self._cliente
    @property
    def listaItens(self):
        return self._listaItens
    
    def addItem(self, item):
        if isinstance(item, ItemPedido):
            self.listaItens.append(item)
        else:
            raise TypeError("O item deve ser uma instância de ItemPedido")
        
    def maquinaOk(self):
        categorias = {
            "gabinete": False,
            "placa_mae": False,
            "processador": False,
            "ssd": False,
            "memoria": False,
            "sistema_operacional": False
        }
        
        for item in self._listaItens:
            codigo = item.produto.codigo
            if 100 <= codigo <= 199:
                categorias["gabinete"] = True
            elif 200 <= codigo <= 299:
                categorias["placa_mae"] = True
            elif 300 <= codigo <= 399:
                categorias["processador"] = True
            elif 400 <= codigo <= 499:
                categorias["ssd"] = True
            elif 500 <= codigo <= 599:
                categorias["memoria"] = True
            elif 600 <= codigo <= 699:
                categorias["sistema_operacional"] = True
        
        return all(categorias.values())
        
    def imprimePedido(self):
        if not self.maquinaOk():
            return False

        print(f'Cliente: {self.cliente.nome}')
        print('Quant - Produto - Preço Unit - Preço Total')
        for item in self._listaItens:
            preco_unitario_com_imposto = item.produto.calculaImposto()
            preco_total = preco_unitario_com_imposto * item.quantidade
            print(f'{item.quantidade} - {item.produto.desc} - {preco_unitario_com_imposto:.2f} - {preco_total:.2f}')
        
        total = sum(item.produto.calculaImposto() * item.quantidade for item in self._listaItens)
        print(f'Valor total: {total:.2f}')
        return True
        
    
class Cliente:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        
    @property
    def nome(self):
        return self._nome
    @property
    def email(self):
        return self._email
    
    def __str__(self):
        return f'{self.nome} - {self.email}'


class ItemPedido:
    def __init__(self, nroItem, produto, quantidade):
        self._nroItem = nroItem
        self._produto = produto
        self._quantidade = quantidade
        
    @property
    def nroItem(self):
        return self._nroItem
    @property
    def produto(self):
        return self._produto
    @property
    def quantidade(self):
        return self._quantidade
    
    
class Produto(ABC):
    def __init__(self, codigo, desc, preco):
        self._codigo = codigo
        self._desc = desc
        self._preco = preco
        
    @property
    def codigo(self):
        return self._codigo
    @property
    def desc(self):
        return self._desc
    @property
    def preco(self):
        return self._preco
    
    @abstractmethod
    def calculaImposto(self):
        pass
    
class ProdutoSoftware(Produto):
    def __init__(self, codigo, desc, preco, versao):
        super().__init__(codigo, desc, preco)
        self._versao = versao
        
    @property
    def versao(self):
        return self._versao
    
    def calculaImposto(self):
        if self.preco <= 399.99:
            return self.preco * 1.05
        elif self.preco >= 400:
            return self.preco * 1.07

class ProdutoHardware(Produto):
    def __init__(self, codigo, desc, preco, nroSerie):
        super().__init__(codigo, desc, preco)
        self._nroSerie = nroSerie
        
    @property
    def nroSerie(self):
        return self._nroSerie
    
    def calculaImposto(self):
        if self.preco <= 499.99:
            return self.preco * 1.06
        elif self.preco >= 500:
            return self.preco * 1.09

if __name__ == "__main__":    
    prod1 = ProdutoHardware(101, 'Gabinete Padrão', 200, '12345')
    prod2 = ProdutoHardware(102, 'Gabinete Gamer', 300, '23451')
    prod3 = ProdutoHardware(201, 'Placa Mãe ASUS ROG', 1_400, '345123')
    prod4 = ProdutoHardware(202, 'Placa Mãe Gigabyte Elite', 1_800, '45123')
    prod5 = ProdutoHardware(301, 'Intel Core I5', 900, '51234')
    prod6 = ProdutoHardware(302, 'AMD Ryzen 7', 700, '67890')
    prod7 = ProdutoHardware(401, 'SSD 256', 200, '78906')
    prod8 = ProdutoHardware(402, 'SSD 512', 300, '89067')
    prod9 = ProdutoHardware(501, 'Pente memória 8GB', 180, '90678')
    prod10 = ProdutoSoftware(601, 'Windows 11 Home Edition', 250, '23H2')

    cliente1 = Cliente('João Santos', 'santos@gmail.com')
    cliente2 = Cliente('Maria Souza', 'souza@gmail.com')

    pedido1 = Pedido(1001, cliente1)
    pedido1.addItem(ItemPedido(1, prod1, 1))
    pedido1.addItem(ItemPedido(2, prod3, 1))
    pedido1.addItem(ItemPedido(3, prod7, 1))
    pedido1.addItem(ItemPedido(4, prod9, 2))
    if not pedido1.imprimePedido():
        print("\nPedido está incompleto")

    pedido2 = Pedido(1002, cliente2)
    pedido2.addItem(ItemPedido(1, prod2, 1))
    pedido2.addItem(ItemPedido(2, prod4, 1))
    pedido2.addItem(ItemPedido(3, prod6, 1))
    pedido2.addItem(ItemPedido(4, prod8, 1))
    pedido2.addItem(ItemPedido(5, prod9, 2))
    pedido2.addItem(ItemPedido(6, prod10, 1))
    if not pedido2.imprimePedido():
        print("\nPedido está incompleto")