import tkinter as tk
from tkinter import ttk, messagebox
import os.path
import pickle

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.avaliacoes = []
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor.isdigit():
            raise ValueError(f"Código inválido: {valor}. Deve ser um número.")
        elif not valor:
            raise ValueError("Código não pode ser vazio.")
        else:
            self.__codigo = valor
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not valor.isalpha():
            raise ValueError(f'Título inválido: {valor}. Deve conter apenas letras.')
        elif not valor:
            raise ValueError("Título não pode ser vazio.")
        else:
            self.__titulo = valor
    
    @property
    def console(self):
        return self.__console
    
    @console.setter
    def console(self, valor):
        self.consoles = ["xbox", "playstation", "switch", "pc"]
        if not valor.lower() in self.consoles:
            raise ValueError(f"Console inválido: {valor}. Deve ser um dos seguintes: {', '.join(self.consoles)}")
        elif not valor:
            raise ValueError("Console não pode ser vazio.")
        else:
            self.__console = valor
            
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, valor):
        self.generos = ["ação", "aventura", "estratégia", "rpg", "esporte", "simulação"]
        if not valor.lower() in self.generos:
            raise ValueError(f"Gênero inválido: {valor}. Deve ser um dos seguintes: {', '.join(self.generos)}")
        elif not valor:
            raise ValueError("Gênero não pode ser vazio.")
        else:
            self.__genero = valor
            
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0 or valor > 500:
            raise ValueError(f"Preço inválido: {valor}. Deve ser maior que ZERO e menor ou igual a 500.")
        elif not valor or valor in ["", " "]:
            raise ValueError("Preço não pode ser vazio.")      
        elif not isinstance(valor, (int, float)):
            raise ValueError(f"Preço inválido: {valor}. Deve ser um número.")
        else:
            self.__preco = float(valor)
    
    def getJogo(self):
        return f"Código: {self.codigo}\
        \nTítulo: {self.titulo}\
        \nConsole: {self.console}\
        \nGênero: {self.genero}\
        \nPreço: R$ {self.preco:.2f}"
        
    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    @avaliacoes.setter
    def avaliacoes(self, valor):
        self.__avaliacoes = valor   
        
    def getJogo(self):
        info = f"Código: {self.codigo}\
        \nTítulo: {self.titulo}\
        \nConsole: {self.console}\
        \nGênero: {self.genero}\
        \nPreço: R$ {self.preco:.2f}"
        if self.avaliacoes and len(self.avaliacoes) > 0:
            media = sum(self.avaliacoes) / len(self.avaliacoes)
            info += f"\nMédia de Avaliação: {media:.2f}"
        return info
        
class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Jogo")
        self.controle = controle
        
        self.frameCodigo = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameTitulo = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameConsole = tk.Frame(self)
        self.frameConsole.pack()
        self.frameGenero = tk.Frame(self)
        self.frameGenero.pack()
        self.framePreco = tk.Frame(self)
        self.framePreco.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        
        self.labelCodigo = tk.Label(self.frameCodigo, text = "Código: ")
        self.labelCodigo.pack(side = "left")
        self.labelTitulo = tk.Label(self.frameTitulo, text = "Título: ")
        self.labelTitulo.pack(side = "left")
        self.labelConsole = tk.Label(self.frameConsole, text = "Console: ")
        self.labelConsole.pack(side = "left")
        self.labelGenero = tk.Label(self.frameGenero, text = "Gênero: ")
        self.labelGenero.pack(side = "left")
        self.labelPreco = tk.Label(self.framePreco, text = "Preço: ")
        self.labelPreco.pack(side = "left")
        
        self.inputCodigo = tk.Entry(self.frameCodigo, width = "10")
        self.inputCodigo.pack(side = "left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width = "10")
        self.inputTitulo.pack(side = "left")
        self.inputConsole = tk.Entry(self.frameConsole, width = "10")
        self.inputConsole.pack(side = "left")
        self.inputGenero = tk.Entry(self.frameGenero, width = "10")
        self.inputGenero.pack(side = "left")
        self.inputPreco = tk.Entry(self.framePreco, width = "10")
        self.inputPreco.pack(side = "left")
        
        self.buttonSubmit = tk.Button(self.frameButton, text = "Enter")
        self.buttonSubmit.pack(side = "left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
        self.buttonClear = tk.Button(self.frameButton, text = "Limpar")
        self.buttonClear.pack(side = "left")
        self.buttonClear.bind("<Button>", controle.clearHandler)
        self.buttonClose = tk.Button(self.frameButton, text = "Fechar")
        self.buttonClose.pack(side = "left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, console, genero, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Consulta de Jogos")
        self.ctrl = controle
        
        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady = 3)
        
        self.labelConsole = tk.Label(self.frameCombos, text = "Console: ")
        self.labelConsole.pack(side = "left")
        self.escolheConsole = tk.StringVar()
        self.comboboxConsole = ttk.Combobox(self.frameCombos, width = 15, values = console, textvariable = self.escolheConsole)
        self.comboboxConsole.pack(side = "left")
        self.comboboxConsole.bind("<<ComboboxSelected>>", self.ctrl.exibeConsole)
        
        self.labelGenero = tk.Label(self.frameCombos, text = "Gênero: ")
        self.labelGenero.pack(side = "left")
        self.escolheGenero = tk.StringVar()
        self.comboboxGenero = ttk.Combobox(self.frameCombos, width = 15, values = genero, textvariable = self.escolheGenero)
        self.comboboxGenero.pack(side = "left")
        self.comboboxGenero.bind("<<ComboboxSelected>>", self.ctrl.exibeGenero)
        
        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, width = 50, height = 15)
        self.textJogos.pack()
        self.textJogos.config(state = tk.DISABLED) # Desabilita o campo de texto para edição

class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Avaliação de Jogos")
        self.ctrl = controle
        
        self.frameCodigo = tk.Frame(self)
        self.frameCodigo.pack(pady = 3)
        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady = 3)
        self.labelCodigo = tk.Label(self.frameCodigo, text = "Código do Jogo: ")
        self.labelCodigo.pack(side = "left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width = "10")
        self.inputCodigo.pack(side = "left")
        
        self.labelAvaliacao = tk.Label(self.frameCombos, text = "Avaliação: ")
        self.labelAvaliacao.pack(side = "left")
        self.escolheAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameCombos, width = 15, values = ["1", "2", "3", "4", "5"], textvariable = self.escolheAvaliacao)
        self.comboboxAvaliacao.pack(side = "left")
        self.comboboxAvaliacao.bind("<<ComboboxSelected>>", self.ctrl.processaAvaliacao)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaPorAvaliacao(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Consulta de Jogos por Avaliação")
        self.ctrl = controle
        
        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady = 3)
        self.labelAvaliacao = tk.Label(self.frameCombos, text = "Avaliação: ")
        self.labelAvaliacao.pack(side = "left")
        self.escolheAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameCombos, width = 15, values = ["1", "2", "3", "4", "5"], textvariable = self.escolheAvaliacao)
        self.comboboxAvaliacao.pack(side = "left")
        self.comboboxAvaliacao.bind("<<ComboboxSelected>>", self.ctrl.exibeJogosPorAvaliacao)
        
        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, width = 50, height = 15)
        self.textJogos.pack()
        self.textJogos.config(state = tk.DISABLED)  
        
class CtrlJogo():
    def __init__(self, controlador):
        self.controlador = controlador
        if not os.path.isfile('jogos.pickle'):
            self.listaJogos = []
        else:
            with open('jogos.pickle', 'rb') as f:
                self.listaJogos = pickle.load(f)
        
    def salvaJogos(self):
        if len(self.listaJogos) > 0:
            with open('jogos.pickle', 'wb') as f:
                pickle.dump(self.listaJogos, f)
                
    def cadastraJogo(self):
        self.limiteIns = LimiteInsereJogo(self)
        
    def avaliaJogo(self):
        self.limiteAval = LimiteAvaliaJogo(self)
        
    def processaAvaliacao(self, event):       
        codigo = self.limiteAval.inputCodigo.get()
        avaliacao = self.limiteAval.escolheAvaliacao.get()
        jogo_encontrado = False
        for jogo in self.listaJogos:
            if jogo.codigo == codigo:
                jogo.avaliacoes.append(int(avaliacao))
                jogo_encontrado = True
                self.limiteAval.mostraJanela("Sucesso", f"Avaliação {avaliacao} adicionada ao jogo {jogo.titulo}.")
                break
        if not jogo_encontrado:
            self.limiteAval.mostraJanela("Erro", f"Jogo com código {codigo} não encontrado.")
        self.limiteAval.inputCodigo.delete(0, len(self.limiteAval.inputCodigo.get()))
        
    def consultaJogo(self):
        self.consoles = []
        self.generos = []
        for jogo in self.listaJogos:
            if (not jogo.console in self.consoles):
                self.consoles.append(jogo.console)
            if (not jogo.genero in self.generos):
                self.generos.append(jogo.genero)
        self.limiteCons = LimiteConsultaJogo(self.consoles, self.generos, self)
        
    def consultaPorAvaliacao(self):
        self.limiteConsAvaliacao = LimiteConsultaPorAvaliacao(self)
        
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()        
        titulo = self.limiteIns.inputTitulo.get()
        console = self.limiteIns.inputConsole.get()
        genero  = self.limiteIns.inputGenero.get()
        preco = self.limiteIns.inputPreco.get()
        
        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.salvaJogos()
            self.listaJogos.append(jogo)
            self.limiteIns.mostraJanela("Sucesso", "Jogo cadastrado com sucesso")
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela("Erro", error)
        
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero. get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco. get())) 
        
    def closeHandler(self, event):
        self.limiteIns.destroy()
        
    def exibeConsole(self, event):
        console = self.limiteCons.escolheConsole.get()
        self.limiteCons.textJogos.config(state = tk.NORMAL)
        self.limiteCons.textJogos.delete(1.0, tk.END)
        for jogo in self.listaJogos:
            if jogo.console == console:
                self.limiteCons.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
        self.limiteCons.textJogos.config(state = tk.DISABLED)   
    
    def exibeGenero(self, event):
        genero = self.limiteCons.escolheGenero.get()
        self.limiteCons.textJogos.config(state = tk.NORMAL)
        self.limiteCons.textJogos.delete(1.0, tk.END)
        for jogo in self.listaJogos:
            if jogo.genero == genero:
                self.limiteCons.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
        self.limiteCons.textJogos.config(state = tk.DISABLED)
        
    def exibeJogosPorAvaliacao(self, event):
        estrela = int(self.limiteConsAvaliacao.escolheAvaliacao.get())
        self.limiteConsAvaliacao.textJogos.config(state=tk.NORMAL)
        self.limiteConsAvaliacao.textJogos.delete(1.0, tk.END)
        for jogo in self.listaJogos:
            if len(jogo.avaliacoes) == 0:
                continue
            media = sum(jogo.avaliacoes) / len(jogo.avaliacoes)
            if 0 <= media <= 1 and estrela == 1:
                self.limiteConsAvaliacao.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
            elif 1 < media <= 2 and estrela == 2:
                self.limiteConsAvaliacao.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
            elif 2 < media <= 3 and estrela == 3:
                self.limiteConsAvaliacao.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
            elif 3 < media <= 4 and estrela == 4:
                self.limiteConsAvaliacao.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
            elif 4 < media <= 5 and estrela == 5:
                self.limiteConsAvaliacao.textJogos.insert(tk.END, jogo.getJogo() + "\n\n")
        self.limiteConsAvaliacao.textJogos.config(state=tk.DISABLED)
        
