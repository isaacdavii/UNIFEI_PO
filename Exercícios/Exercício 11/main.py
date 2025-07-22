import tkinter as tk
import jogo as jg

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.jogoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)
        
        self.jogoMenu.add_command(label = "Cadastrar", command = self.controle.cadastraJogo)
        self.jogoMenu.add_command(label = "Consultar", command = self.controle.consultaJogo)
        self.jogoMenu.add_command(label = "Consultar por Avaliação", command = self.controle.consultaPorAvaliacao)
        self.jogoMenu.add_command(label = "Avaliar", command = self.controle.avaliaJogo)
        self.menubar.add_cascade(label = "Jogo", menu = self.jogoMenu)
        
        self.sairMenu.add_command(label = "Salvar", command = self.controle.salvaDados)
        self.menubar.add_cascade(label = "Sair", menu = self.sairMenu)
        
        self.root.config(menu = self.menubar)
        
class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlJogo = jg.CtrlJogo(self)
        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Cadastro de Jogos")
        self.root.mainloop()
        
    def cadastraJogo(self):
        self.ctrlJogo.cadastraJogo()
        
    def consultaJogo(self):
        self.ctrlJogo.consultaJogo()
        
    def consultaPorAvaliacao(self):
        self.ctrlJogo.consultaPorAvaliacao()
        
    def avaliaJogo(self):
        self.ctrlJogo.avaliaJogo()
    
    def salvaDados(self):
        self.ctrlJogo.salvaJogos()
        self.root.destroy()
        
if __name__ == "__main__":
    c = ControlePrincipal()