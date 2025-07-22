import tkinter as tk
import comanda as cmd

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Sistema de Comanda - Restaurante Comida Boa")

        self.menubar = tk.Menu(self.root)
        self.comandaMenu = tk.Menu(self.menubar, tearoff=0)
        self.comandaMenu.add_command(label = "Lançar Comanda", command = self.controle.lancarComanda)
        self.comandaMenu.add_command(label = "Imprimir Comanda", command = self.controle.imprimirComanda)
        self.comandaMenu.add_command(label = "Calcular Faturamento", command = self.controle.calcularFaturamento)
        self.menubar.add_cascade(label = "Comanda", menu = self.comandaMenu)

        self.sairMenu = tk.Menu(self.menubar, tearoff=0)
        self.sairMenu.add_command(label = "Sair", command = self.controle.sair)
        self.menubar.add_cascade(label = "Sair", menu = self.sairMenu)

        self.root.config(menu = self.menubar)

        self.framePrincipal = tk.Frame(self.root, padx = 20, pady = 20)
        self.framePrincipal.pack(expand = True, fill = "both")

        self.labelTitulo = tk.Label(
            self.framePrincipal,
            text="Restaurante Comida Boa",
            font=("Arial", 16, "bold"),
        )
        self.labelTitulo.pack(pady = 10)

        # Informações do restaurante na tela inicial
        self.labelInfo = tk.Label(
            self.framePrincipal,
            text="Sistema de Controle de Comanda\n\n"
            + "Refeição adulto: R$ 40,00\n"
            + "Refeição criança (até 7 anos): R$ 20,00\n\n"
            + "Use o menu acima para:\n"
            + "• Lançar itens na comanda\n"
            + "• Imprimir detalhes da comanda\n"
            + "• Calcular faturamento total",
            font=("Arial", 10),
            justify="left",
        )
        self.labelInfo.pack(pady = 20)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlComanda = cmd.CtrlComanda()
        self.limite = LimitePrincipal(self.root, self)
        self.root.mainloop()

    def lancarComanda(self):
        self.ctrlComanda.lancarComanda()

    def imprimirComanda(self):
        self.ctrlComanda.imprimirComanda()

    def calcularFaturamento(self):
        self.ctrlComanda.calcularFaturamento()

    def sair(self):
        self.ctrlComanda.salvaComandas()
        self.root.destroy()

if __name__ == "__main__":
    c = ControlePrincipal()
