import tkinter as tk
from tkinter import messagebox

class Musica:
    def __init__(self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    @property
    def nroFaixa(self):
        return self.__nroFaixa

class LimiteInsereMusica(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x120')
        self.title("Música")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameFaixa = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameFaixa.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text = "Título da música: ")
        self.labelTitulo.pack(side = "left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width = 20)
        self.inputTitulo.pack(side = "left")

        self.labelFaixa = tk.Label(self.frameFaixa, text = "Número da faixa: ")
        self.labelFaixa.pack(side = "left")
        self.inputFaixa = tk.Entry(self.frameFaixa, width = 5)
        self.inputFaixa.pack(side = "left")

        self.buttonSubmit = tk.Button(self.frameButton, text = "Cadastrar")
        self.buttonSubmit.pack(side = "left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlMusica:
    def __init__(self):
        self.listaMusicas = []

    def getMusica(self, nome):
        for musica in self.listaMusicas:
            if musica.titulo.lower() == nome.lower():
                return musica
        return None

    def insereMusica(self):
        self.limiteIns = LimiteInsereMusica(self)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        nroFaixa = self.limiteIns.inputFaixa.get()
        if not (titulo and nroFaixa):
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos!')
            return
        if self.getMusica(titulo):
            self.limiteIns.mostraJanela('Erro', 'Música já cadastrada!')
        else:
            musica = Musica(titulo, nroFaixa)
            self.listaMusicas.append(musica)
            self.limiteIns.mostraJanela('Sucesso', 'Música cadastrada com sucesso!')
        self.limiteIns.inputTitulo.delete(0, tk.END)
        self.limiteIns.inputFaixa.delete(0, tk.END)

    def fechaHandler(self, event):
        self.limiteIns.destroy()