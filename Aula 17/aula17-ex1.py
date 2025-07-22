import tkinter as tk
from tkinter import messagebox

class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

class View():
    def __init__(self, master, controller):
        self.controller = controller # referência ao controlador
        self.janela = tk.Frame(master) # janela principal
        self.janela.pack() # configura a janela principal
        self.frame1 = tk.Frame(self.janela) # frame para o nome
        self.frame2 = tk.Frame(self.janela) # frame para o email
        self.frame1.pack() # configura o frame do nome
        self.frame2.pack() # configura o frame do email
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.janela,text="Salva")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)            

        self.buttonList = tk.Button(self.janela,text="Lista")
        self.buttonList.pack(side="left")
        self.buttonList.bind("<Button>", controller.listHandler)
        
    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk() # cria a janela principal
        self.root.geometry('300x100') # define o tamanho da janela
        self.listaClientes = [] # lista para armazenar os clientes

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) # cria a view

        self.root.title("Exemplo MVC") # define o título da janela principal
        # Inicia o mainloop
        self.root.mainloop() # inicia o loop de eventos da janela

    def salvaHandler(self, event): # método para salvar o cliente
        # Obtém os dados do cliente a partir dos campos de entrada
        nomeCli = self.view.inputText1.get() # obtém o nome do cliente
        if not nomeCli:
            self.view.mostraJanela('Erro', 'Nome não pode ser vazio')
            return
        emailCli = self.view.inputText2.get() # obtém o email do cliente
        if not emailCli:
            self.view.mostraJanela('Erro', 'Email não pode ser vazio')
            return
        cliente = ModelCliente(nomeCli, emailCli) # cria um novo cliente com os dados obtidos
        self.listaClientes.append(cliente) # adiciona o cliente à lista de clientes
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso') # mostra mensagem de sucesso
        self.clearHandler(event) # limpa os campos de entrada após o cadastro

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get())) # limpa o campo de entrada do nome
        self.view.inputText2.delete(0, len(self.view.inputText2.get())) # limpa o campo de entrada do email
        
    def listHandler(self, event):
        self.msg = 'Clientes Cadastrados:\n'
        if not self.listaClientes:
            self.view.mostraJanela('Lista', 'Nenhum cliente cadastrado')
        else:
            for cli in self.listaClientes:
                self.msg += cli.nome + ' - ' + cli.email + '\n'
            self.view.mostraJanela('Lista', self.msg)
        

if __name__ == '__main__':
    c = Controller()