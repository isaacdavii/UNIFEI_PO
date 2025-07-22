import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Produto:
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        
    @property
    def codigo(self):
        return self.__codigo
    @property
    def descricao(self):
        return self.__descricao
    @property
    def valor(self):
        return self.__valor
    
class LimiteInsereProdutos(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title('Produto')
        self.controle = controle
        
        self.frameCod = tk.Frame(self)
        self.frameCod.pack()
        self.frameDesc = tk.Frame(self)
        self.frameDesc.pack()
        self.frameValor = tk.Frame(self)
        self.frameValor.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        
        self.labelCod = tk.Label(self.frameCod, text = 'Código:')
        self.labelCod.pack(side = 'left')
        self.labelDesc = tk.Label(self.frameDesc, text = 'Descrição:')
        self.labelDesc.pack(side = 'left')
        self.labelValor = tk.Label(self.frameValor, text = 'Valor:')
        self.labelValor.pack(side = 'left')
        
        self.inputCod = tk.Entry(self.frameCod, width = 10)
        self.inputCod.pack(side = 'left')
        self.inputDesc = tk.Entry(self.frameDesc, width = 20)
        self.inputDesc.pack(side = 'left')
        self.inputValor = tk.Entry(self.frameValor, width = 10)
        self.inputValor.pack(side = 'left')
        
        self.buttonSubmit = tk.Button(self.frameButton, text = 'Cadastrar')
        self.buttonSubmit.pack(side = 'left')
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
        
        self.buttonClear = tk.Button(self.frameButton, text = 'Limpar')
        self.buttonClear.pack(side = 'left')
        self.buttonClear.bind("<Button>", controle.clearHandler)
        
        self.buttonClose = tk.Button(self.frameButton, text = 'Fechar')
        self.buttonClose.pack(side = 'left')
        self.buttonClose.bind("<Button>", controle.closeHandler)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaProdutos(tk.Toplevel):
    def __init__(self, controle, listaProdutos):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title('Consulta de Produtos')
        self.controle = controle
        
        self.listaProdutos = listaProdutos
        self.frameCod = tk.Frame(self)
        self.frameCod.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        
        self.labelCod = tk.Label(self.frameCod, text = 'Código:')
        self.labelCod.pack(side = 'left')
        self.inputCod = tk.Entry(self.frameCod, width = 10)
        self.inputCod.pack(side = 'left')
        
        self.buttonSubmit = tk.Button(self.frameButton, text = 'Consultar')
        self.buttonSubmit.pack(side = 'left')
        self.buttonSubmit.bind('<Button>', controle.consultaHandler)
        
        self.buttonClose = tk.Button(self.frameButton, text = 'Fechar')
        self.buttonClose.pack(side = 'left')
        self.buttonClose.bind('<Button>', controle.closeHandlerConsulta)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraProdutos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Produtos', str)

class CtrlProduto:
    def __init__(self):
        if not os.path.isfile('produtos.pickle'):
            self.listaProdutos = []
        else:
            with open('produtos.pickle', 'rb') as f:
                self.listaProdutos = pickle.load(f)
                
    def salvaProdutos(self):
        if len(self.listaProdutos) > 0:
            with open('produtos.pickle', 'wb') as f:
                pickle.dump(self.listaProdutos, f)
                
    def getListaProdutos(self):
        return self.listaProdutos

    def getProduto(self, codigo):
        for produto in self.listaProdutos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def insereProduto(self):
        self.limiteIns = LimiteInsereProdutos(self)
        
    def consultaProduto(self):
        self.limiteCons = LimiteConsultaProdutos(self, self.listaProdutos)
        
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCod.get()
        descricao = self.limiteIns.inputDesc.get()
        valor = self.limiteIns.inputValor.get()
        
        if not codigo or not descricao or not valor:
            self.limiteIns.mostraJanela('Erro', 'Todos os campos devem ser preenchidos!')
            return
        
        if self.getProduto(codigo):
            self.limiteIns.mostraJanela('Erro', 'Produto já cadastrado!')
            return
        
        try:
            valor = float(valor)
        except ValueError:
            self.limiteIns.mostraJanela('Erro', 'Valor deve ser um número!')
            return
        
        produto = Produto(codigo, descricao, valor)
        self.listaProdutos.append(produto)
        self.salvaProdutos()
        
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso!')
        self.clearHandler()
            
    def clearHandler(self):
        self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
        self.limiteIns.inputDesc.delete(0, len(self.limiteIns.inputDesc.get()))
        self.limiteIns.inputValor.delete(0, len(self.limiteIns.inputValor.get()))
    
    def closeHandler(self, event):
        self.limiteIns.destroy()
        self.limiteIns = None
        
    def closeHandlerConsulta(self, event):
        self.limiteCons.destroy()
        
    def consultaHandler(self, event):
        codigo = self.limiteCons.inputCod.get()
        produto = self.getProduto(codigo)
        if produto:
            str = f"Código: {produto.codigo}\nDescrição: {produto.descricao}\nValor: {produto.valor}"
            self.limiteMostra = LimiteMostraProdutos(str)
        else:
            self.limiteCons.mostraJanela('Erro', 'Produto não encontrado!')