import tkinter as tk
from tkinter import messagebox, ttk
import os.path
import pickle

class Produto:
    def __init__(self, codigo, descricao, preco):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

class ItemComanda:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor

    def getSubtotal(self):
        return self.__produto.preco * self.__quantidade

class Comanda:
    def __init__(self, numero):
        self.__numero = numero
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def itens(self):
        return self.__itens

    def adicionaItem(self, produto, quantidade):
        for item in self.__itens:
            if item.produto.codigo == produto.codigo:
                item.quantidade += quantidade
                return
        novoItem = ItemComanda(produto, quantidade)
        self.__itens.append(novoItem)

    def getTotal(self):
        total = 0
        for item in self.__itens:
            total += item.getSubtotal()
        return total

    def getTotalRefeicoes(self):
        total = 0
        for item in self.__itens:
            if item.produto.codigo in [901, 902]:
                total += item.getSubtotal()
        return total

    def getTotalProdutos(self):
        total = 0
        for item in self.__itens:
            if item.produto.codigo not in [901, 902]:
                total += item.getSubtotal()
        return total

class LimiteLancarComanda(tk.Toplevel):
    def __init__(self, controle, listaProdutos):
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("Lançar Comanda")
        self.controle = controle

        self.frameNumero = tk.Frame(self)
        self.frameNumero.pack(pady = 10)
        self.frameProduto = tk.Frame(self)
        self.frameProduto.pack(pady = 10)
        self.frameQuantidade = tk.Frame(self)
        self.frameQuantidade.pack(pady=10)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(pady = 20)
                     
        self.labelNumero = tk.Label(self.frameNumero, text = "Número da Comanda:")
        self.labelNumero.pack(side = "left")
        self.inputNumero = tk.Entry(self.frameNumero, width = 15)
        self.inputNumero.pack(side = "left", padx = 5)

        self.labelProduto = tk.Label(self.frameProduto, text = "Produto:")
        self.labelProduto.pack(side = "left")
        self.comboProduto = ttk.Combobox(self.frameProduto, width = 30, state = "readonly")
        self.comboProduto.pack(side = "left", padx = 5)

        valores = []
        for produto in listaProdutos:
            valores.append(f"{produto.codigo} - {produto.descricao} - R$ {produto.preco:.2f}")
        self.comboProduto["values"] = valores

        self.labelQuantidade = tk.Label(self.frameQuantidade, text = "Quantidade:")
        self.labelQuantidade.pack(side = "left")
        self.inputQuantidade = tk.Entry(self.frameQuantidade, width = 10)
        self.inputQuantidade.pack(side = "left", padx = 5)

        self.buttonAdicionar = tk.Button(self.frameButton, text = "Adicionar Item")
        self.buttonAdicionar.pack(side = "left", padx = 5)
        self.buttonAdicionar.bind("<Button>", controle.adicionarItemHandler)

        self.buttonFechar = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFechar.pack(side = "left", padx = 5)
        self.buttonFechar.bind("<Button>", controle.fecharLancarHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteImprimirComanda(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry("350x250")
        self.title("Imprimir Comanda")
        self.controle = controle

        self.frameNumero = tk.Frame(self)
        self.frameNumero.pack(pady = 20)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(pady = 20)
        
        self.labelNumero = tk.Label(self.frameNumero, text = "Número da Comanda:")
        self.labelNumero.pack(side="left")
        self.inputNumero = tk.Entry(self.frameNumero, width = 15)
        self.inputNumero.pack(side="left", padx = 5)

        self.buttonImprimir = tk.Button(self.frameButton, text = "Imprimir")
        self.buttonImprimir.pack(side="left", padx = 5)
        self.buttonImprimir.bind("<Button>", controle.imprimirComandaHandler)

        self.buttonFechar = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFechar.pack(side="left", padx=5)
        self.buttonFechar.bind("<Button>", controle.fecharImprimirHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlComanda:
    def __init__(self):
        self.listaProdutos = [
            Produto(901, "Refeicao", 40),
            Produto(902, "Refeicao Crianca", 20),
            Produto(903, "Guarana lata", 6),
            Produto(904, "Coca Cola lata", 6),
            Produto(905, "Suco laranja 400 ml", 8),
            Produto(906, "Cerveja Heineken lata", 8),
            Produto(907, "Agua mineral 500 ml", 4),
            Produto(908, "Sorvete Kibon", 8),
            Produto(909, "Chocolate Alpino", 6),
            Produto(910, "Chocolate Lacta", 5),
        ]

        if not os.path.isfile("comandas.pickle"):
            self.listaComandas = []
        else:
            with open("comandas.pickle", "rb") as f:
                self.listaComandas = pickle.load(f)

    def salvaComandas(self):
        if len(self.listaComandas) > 0:
            with open("comandas.pickle", "wb") as f:
                pickle.dump(self.listaComandas, f)

    def getComanda(self, numero):
        for comanda in self.listaComandas:
            if comanda.numero == numero:
                return comanda
        return None

    def getProduto(self, codigo):
        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                return produto
        return None

    def lancarComanda(self):
        self.limiteLancar = LimiteLancarComanda(self, self.listaProdutos)

    def imprimirComanda(self):
        self.limiteImprimir = LimiteImprimirComanda(self)

    def calcularFaturamento(self):
        totalRefeicoes = 0
        totalProdutos = 0

        for comanda in self.listaComandas:
            totalRefeicoes += comanda.getTotalRefeicoes()
            totalProdutos += comanda.getTotalProdutos()

        totalGeral = totalRefeicoes + totalProdutos

        msg = f"FATURAMENTO TOTAL:\n\n"
        msg += f"Total faturado com refeições: R$ {totalRefeicoes:.2f}\n"
        msg += f"Total faturado com produtos: R$ {totalProdutos:.2f}\n"
        msg += f"Total geral: R$ {totalGeral:.2f}"

        messagebox.showinfo("Faturamento", msg)

    def adicionarItemHandler(self, event):
        numero = self.limiteLancar.inputNumero.get().strip()
        produto_selecionado = self.limiteLancar.comboProduto.get()
        quantidade_str = self.limiteLancar.inputQuantidade.get().strip()

        if not numero:
            self.limiteLancar.mostraJanela("Erro", "Informe o número da comanda!")
            return

        if not produto_selecionado:
            self.limiteLancar.mostraJanela("Erro", "Selecione um produto!")
            return

        if not quantidade_str:
            self.limiteLancar.mostraJanela("Erro", "Informe a quantidade!")
            return

        try:
            quantidade = int(quantidade_str)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            self.limiteLancar.mostraJanela("Erro", "Quantidade deve ser um número inteiro positivo!")
            return

        codigo = int(produto_selecionado.split(" - ")[0]) # Extrai o código do produto
        produto = self.getProduto(codigo)
        comanda = self.getComanda(numero)
        if not comanda:
            comanda = Comanda(numero)
            self.listaComandas.append(comanda)

        comanda.adicionaItem(produto, quantidade)
        self.salvaComandas()
        self.limiteLancar.mostraJanela("Sucesso", f"Item adicionado à comanda {numero}!")
        self.limiteLancar.inputQuantidade.delete(0, tk.END)
        self.limiteLancar.comboProduto.set("")

    def imprimirComandaHandler(self, event):
        numero = self.limiteImprimir.inputNumero.get().strip()
        if not numero:
            self.limiteImprimir.mostraJanela("Erro", "Informe o número da comanda!")
            return

        comanda = self.getComanda(numero)
        if not comanda:
            self.limiteImprimir.mostraJanela("Erro", "Comanda não encontrada!")
            return

        detalhes = f"COMANDA Nº {comanda.numero}\n\n"
        detalhes += "ITENS:\n"

        for item in comanda.itens:
            detalhes += f"- {item.produto.descricao} - Qtd: {item.quantidade} - R$ {item.getSubtotal():.2f}\n"

        detalhes += f"\nVALOR TOTAL: R$ {comanda.getTotal():.2f}"

        messagebox.showinfo("Detalhes da Comanda", detalhes)
        self.limiteImprimir.inputNumero.delete(0, tk.END)

    def fecharLancarHandler(self, event):
        self.limiteLancar.destroy()

    def fecharImprimirHandler(self, event):
        self.limiteImprimir.destroy()
