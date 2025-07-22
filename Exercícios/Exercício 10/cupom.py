import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class CupomFiscal:
    def __init__(self, nroCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = []
        
    @property
    def nroCupom(self):
        return self.__nroCupom
    @property
    def itensCupom(self):
        return self.__itensCupom
    
    def adiciona_item(self, produto):
        self.__itensCupom.append(produto)
        
class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle, listaProdutos):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title('Cupom Fiscal')
        self.controle = controle
        
        self.frameNro = tk.Frame(self)
        self.frameNro.pack()
        self.frameProd = tk.Frame(self)
        self.frameProd.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()
        
        self.labelNro = tk.Label(self.frameNro, text = 'Número do Cupom:')
        self.labelNro.pack(side = tk.LEFT)
        self.entryNro = tk.Entry(self.frameNro, width = 15)
        self.entryNro.pack(side = tk.LEFT)
        
        self.labelProduto = tk.Label(self.frameProd, text = 'Selecione o produto')
        self.labelProduto.pack(side = tk.LEFT)
        self.listaboxProdutos = tk.Listbox(self.frameProd, width = 30, height = 10)
        self.listaboxProdutos.pack(side = tk.LEFT)
        self.listaboxProdutos.bind('<<ListboxSelect>>', controle.on_select)
        controle.populate_produtos(listaProdutos, self.listaboxProdutos)
        self.selected_produto = None
        
        self.buttonAddProd = tk.Button(self.frameProd, text = 'Adicionar Produto')
        self.buttonAddProd.pack(side = tk.LEFT)
        self.buttonAddProd.bind('<Button>', controle.addProdutoHandler)
        
        self.buttonCria = tk.Button(self.frameButton, text = 'Criar Cupom')
        self.buttonCria.pack(side = tk.LEFT)
        self.buttonCria.bind('<Button>', controle.criarCupomHandler)
        
        self.buttonClose = tk.Button(self.frameButton, text = 'Fechar')
        self.buttonClose.pack(side = tk.LEFT)
        self.buttonClose.bind('<Button>', controle.fecharHandler)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
        
class LimiteConsultaCupom(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title('Consulta Cupom Fiscal')
        self.controle = controle
        
        self.frameNro = tk.Frame(self)
        self.frameNro.pack(pady = 10)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(pady = 10)
        
        self.labelNro = tk.Label(self.frameNro, text = 'Número do Cupom:')
        self.labelNro.pack(side = tk.LEFT)
        self.entryNro = tk.Entry(self.frameNro, width = 15)
        self.entryNro.pack(side = tk.LEFT)
        
        self.buttonConsulta = tk.Button(self.frameButton, text = 'Consultar Cupom')
        self.buttonConsulta.pack(side = tk.LEFT)
        self.buttonConsulta.bind('<Button>', controle.consultarCupomHandler)
        
        self.buttonClose = tk.Button(self.frameButton, text = 'Fechar')
        self.buttonClose.pack(side = tk.LEFT)
        self.buttonClose.bind('<Button>', controle.fecharHandlerConsulta)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlCupomFiscal:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        if not os.path.isfile('cupom_fiscal.pickle'):
            self.listaCupons = []
        else:    
            with open('cupom_fiscal.pickle', 'rb') as f:
                self.listaCupons = pickle.load(f)
                
    def salvaCupons(self):
        if len(self.listaCupons) > 0:
            with open('cupom_fiscal.pickle', 'wb') as f:
                pickle.dump(self.listaCupons, f)
    
    def insereCupom(self):
        listaProdutos = self.ctrlPrincipal.ctrlProduto.listaProdutos  
        if not listaProdutos:
            messagebox.showinfo("Erro", "Cadastre um produto primeiro!")
            return
        self.limiteIns = LimiteInsereCupom(self, listaProdutos)

    def criarCupomHandler(self, event):
        nroCupom = self.limiteIns.entryNro.get().strip()
        if not nroCupom:
            messagebox.showinfo("Erro", "Informe o número do cupom!")
            return
        cupom = next((c for c in self.listaCupons if c.nroCupom == nroCupom), None)
        if not cupom:
            messagebox.showinfo("Erro", "Adicione pelo menos um produto antes de criar o cupom!")
            return
        if len(cupom.itensCupom) == 0:
            messagebox.showinfo("Erro", "Adicione pelo menos um produto antes de criar o cupom!")
            return
        
        cupom = CupomFiscal(nroCupom)
        self.listaCupons.append(cupom)
        self.salvaCupons()
        
        self.limiteIns.mostraJanela("Sucesso", "Cupom criado com sucesso!")
        self.clearHandler()
        self.limiteIns.entryNro.delete(0, tk.END)

    def addProdutoHandler(self, event):
        if not self.limiteIns.selected_produto:
            messagebox.showinfo("Erro", "Selecione um produto primeiro!")
            return
        nroCupom = self.limiteIns.entryNro.get().strip()
        if not nroCupom:
            messagebox.showinfo("Erro", "Informe o número do cupom!")
            return
        cupom = next((c for c in self.listaCupons if c.nroCupom == nroCupom), None)
        if not cupom:
            cupom = CupomFiscal(nroCupom)
            self.listaCupons.append(cupom)
            
        cupom.adiciona_item(self.limiteIns.selected_produto)
        self.salvaCupons()
        messagebox.showinfo("Sucesso", "Produto adicionado ao cupom com sucesso!")
        
    def consultarCupomHandler(self, event=None):
        nroCupom = self.limiteCons.entryNro.get().strip()
        if not nroCupom:
            messagebox.showinfo("Erro", "Informe o número do cupom!")
            return
        cupom = next((c for c in self.listaCupons if c.nroCupom == nroCupom), None)
        if not cupom:
            messagebox.showinfo("Erro", "Cupom não encontrado!")
            return

        agrupados = {}
        for item in cupom.itensCupom:
            cod = item.codigo
            if cod not in agrupados:
                agrupados[cod] = {"descricao": item.descricao, "valor": item.valor, "quantidade": 1}
            else:
                agrupados[cod]["quantidade"] += 1

        detalhes = f"Número do Cupom: {cupom.nroCupom}\nItens:\n"
        total = 0
        for cod, info in agrupados.items():
            subtotal = info["quantidade"] * info["valor"]
            detalhes += f" - {cod} - {info['descricao']} - Qtd: {info['quantidade']} - R$ {info['valor']:.2f} - Subtotal: R$ {subtotal:.2f}\n"
            total += subtotal
        detalhes += f"\nValor total do cupom: R$ {total:.2f}"
        messagebox.showinfo("Detalhes do Cupom", detalhes)
        
        self.limiteCons.entryNro.delete(0, tk.END)
        
    def on_select(self, event):
        try:
            index = self.limiteIns.listaboxProdutos.curselection()[0]
            selecionado = self.limiteIns.listaboxProdutos.get(index)
            codigo = selecionado.split(' - ')[0].strip()
            produto = next((p for p in self.ctrlPrincipal.ctrlProduto.listaProdutos if str(p.codigo) == codigo), None)
            self.limiteIns.selected_produto = produto
        except IndexError:
            self.limiteIns.selected_produto = None
            messagebox.showinfo("Erro", "Selecione um produto primeiro!")
            return
        
    def consultaCupom(self):
        self.limiteCons = LimiteConsultaCupom(self)
        
    def populate_produtos(self, listaProdutos, listbox):
        listbox.delete(0, tk.END)
        for produto in listaProdutos:
            listbox.insert(tk.END, f"{produto.codigo} - {produto.descricao} - {produto.valor:.2f}")
            
    def clearHandler(self):
        self.limiteIns.entryNro.delete(0, tk.END)
        self.limiteIns.listaboxProdutos.selection_clear(0, tk.END)
        self.limiteIns.selected_produto = None
        
    def fecharHandler(self, event):
        self.limiteIns.destroy()        
        
    def fecharHandlerConsulta(self, event):
        self.limiteCons.destroy()