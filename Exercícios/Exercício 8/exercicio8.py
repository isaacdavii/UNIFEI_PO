import tkinter as tk
from tkinter import messagebox, simpledialog


class ModelCliente:
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def codigo(self):
        return self.__codigo


class View:
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.labelInfo1 = tk.Label(self.frame1, text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3, text="Código: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")
        self.labelInfo3.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")

        self.buttonSubmit = tk.Button(self.janela, text="Salvar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)

        self.buttonClear = tk.Button(self.janela, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonList = tk.Button(self.janela, text="Listar")
        self.buttonList.pack(side="left")
        self.buttonList.bind("<Button>", controller.listHandler)

        self.buttonSearch = tk.Button(self.janela, text="Buscar")
        self.buttonSearch.pack(side="left")
        self.buttonSearch.bind("<Button>", controller.searchHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.listaClientes = []

        self.view = View(self.root, self)
        self.root.title("Exemplo MVC")

        self.root.mainloop()

    def salvaHandler(self, event):

        nomeCli = self.view.inputText1.get()
        if not nomeCli:
            self.view.mostraJanela("Erro", "Nome não pode ser vazio")
            return
        emailCli = self.view.inputText2.get()
        if not emailCli:
            self.view.mostraJanela("Erro", "Email não pode ser vazio")
            return
        codigoCli = self.view.inputText3.get()
        if not codigoCli:
            self.view.mostraJanela("Erro", "Código não pode ser vazio")
            return

        cliente = ModelCliente(nomeCli, emailCli, codigoCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela("Sucesso", "Cliente cadastrado com sucesso")
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def listHandler(self, event):
        self.msg = "Clientes Cadastrados:\n"
        if not self.listaClientes:
            self.view.mostraJanela("Lista", "Nenhum cliente cadastrado")
        else:
            for cli in self.listaClientes:
                self.msg += cli.nome + " - " + cli.email + " - " + cli.codigo + "\n"
            self.view.mostraJanela("Lista", self.msg)

    def searchHandler(self, event):
        codigoCli = simpledialog.askstring(
            "Buscar Cliente", "Digite o código do cliente:", parent=self.root
        )
        if codigoCli is None:
            return
        if not codigoCli:
            self.view.mostraJanela("Erro", "Código não pode ser vazio!")
            return
        for cli in self.listaClientes:
            if cli.codigo == codigoCli:
                self.view.mostraJanela(
                    "Busca", f"Cliente encontrado: {cli.nome} - {cli.email}"
                )
                return
        self.view.mostraJanela("Busca", "Código não cadastrado!")


if __name__ == "__main__":
    c = Controller()
