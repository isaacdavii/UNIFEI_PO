import tkinter as tk
import produto as pd
import cupom as cp

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        
        self.produtoMenu.add_command(label = 'Cadastrar', command = self.controle.insereProduto)
        self.produtoMenu.add_command(label = 'Consultar', command = self.controle.consultaProduto)
        self.menubar.add_cascade(label = 'Produto', menu = self.produtoMenu)
        
        self.cupomMenu.add_command(label = 'Criar', command = self.controle.insereCupom)
        self.cupomMenu.add_command(label = 'Consultar', command = self.controle.consultaCupom)
        self.menubar.add_cascade(label = 'Cupom Fiscal', menu = self.cupomMenu)
        self.root.config(menu = self.menubar)
        
class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlProduto = pd.CtrlProduto()
        self.ctrlCupom = cp.CtrlCupomFiscal(self)
        
        self.limite = LimitePrincipal(self.root, self)
        self.root.title('Mercadinho')
        self.root.mainloop()
        
    def insereProduto(self):
        self.ctrlProduto.insereProduto()
        
    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()
        
    def insereCupom(self):
        self.ctrlCupom.insereCupom()
        
    def consultaCupom(self):    
        self.ctrlCupom.consultaCupom()
        
if __name__ == '__main__':
    c = ControlePrincipal()