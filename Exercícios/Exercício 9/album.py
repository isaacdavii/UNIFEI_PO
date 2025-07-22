import tkinter as tk
from tkinter import ttk, messagebox
from artista import Artista
from musica import Musica

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []

    @property
    def titulo(self):
        return self.__titulo
    @property
    def artista(self):
        return self.__artista
    @property
    def ano(self):
        return self.__ano
    @property
    def faixas(self):
        return self.__faixas

    def adiciona_faixa(self, musica):
        self.__faixas.append(musica)

class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('700x600')
        self.title("Álbum")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameArtistasColetanea = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameAno.pack()
        self.frameArtista.pack()
        self.frameArtistasColetanea.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text = "Título do álbum: ")
        self.labelTitulo.pack(side = "left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width = 30)
        self.inputTitulo.pack(side = "left")

        self.labelAno = tk.Label(self.frameAno, text = "Ano: ")
        self.labelAno.pack(side = "left")
        self.inputAno = tk.Entry(self.frameAno, width = 10)
        self.inputAno.pack(side = "left")

        self.labelArtista = tk.Label(self.frameArtista, text = "Artista: ")
        self.labelArtista.pack(side = "left")
        self.escolhaArtista = tk.StringVar()
        self.comboboxArtista = ttk.Combobox(self.frameArtista, width = 25, textvariable = self.escolhaArtista)
        self.comboboxArtista.pack(side = "left")
        self.comboboxArtista['values'] = ["Vários artistas"] + listaArtistas
        self.comboboxArtista.bind("<<ComboboxSelected>>", controle.atualizaArtistasColetanea)

        self.labelArtistasColetanea = tk.Label(self.frameArtistasColetanea, text = "Selecione os artistas (coletânea): ")
        self.listboxArtistas = tk.Listbox(self.frameArtistasColetanea, selectmode = tk.MULTIPLE, width = 30)
        self.labelArtistasColetanea.pack(side = "left")
        self.listboxArtistas.pack(side = "left")
        self.frameArtistasColetanea.pack_forget()

        self.labelMusicas = tk.Label(self.frameMusicas, text = "Selecione as músicas:")
        self.labelMusicas.pack(side = "left")
        self.listboxMusicas = tk.Listbox(self.frameMusicas, selectmode = tk.MULTIPLE, width = 40)
        self.listboxMusicas.pack(side = "left")
        
        self.listboxArtistas.bind("<<ListboxSelect>>", controle.atualizaMusicas)

        self.buttonCria = tk.Button(self.frameButton, text = "Cadastrar Álbum")
        self.buttonCria.pack(side = "left")
        self.buttonCria.bind("<Button>", controle.criaAlbumHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle, listaAlbuns):
        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consultar Álbum")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text = "Título do álbum: ")
        self.labelTitulo.pack(side = "left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width = 25)
        self.inputTitulo.pack(side = "left")

        self.buttonConsulta = tk.Button(self.frameButton, text = "Consultar")
        self.buttonConsulta.pack(side = "left")
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlAlbum:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.listaAlbuns = []

    def getAlbum(self, titulo):
        for album in self.listaAlbuns:
            if album.titulo.lower() == titulo.lower():
                return album
        return None
    
    def atualizaArtistasColetanea(self, event):
        escolha = self.limiteIns.escolhaArtista.get()
        if escolha == "Vários artistas":
            self.limiteIns.frameArtistasColetanea.pack()
            self.limiteIns.listboxArtistas.delete(0, tk.END)
            for nome in [a.nome for a in self.ctrlPrincipal.ctrlArtista.listaArtistas]:
                self.limiteIns.listboxArtistas.insert(tk.END, nome)
        else:
            self.limiteIns.frameArtistasColetanea.pack_forget()
        self.atualizaMusicas()
        
    def atualizaMusicas(self, event = None):
        self.limiteIns.listboxMusicas.delete(0, tk.END)
        escolha = self.limiteIns.escolhaArtista.get()
        musicas = []
        if escolha == "Vários artistas":
            indices = self.limiteIns.listboxArtistas.curselection()
            artistas = [self.ctrlPrincipal.ctrlArtista.listaArtistas[i] for i in indices]
            for artista in artistas:
                for musica in artista.musicas:
                    musicas.append(f"{musica.nroFaixa}. {musica.titulo} ({artista.nome})")
        else:
            artista = self.ctrlPrincipal.ctrlArtista.getArtista(escolha)
            if artista:
                for musica in artista.musicas:
                    musicas.append(f"{musica.nroFaixa}. {musica.titulo} ({artista.nome})")
        for m in musicas:
            self.limiteIns.listboxMusicas.insert(tk.END, m)
        
    def insereAlbum(self):
        listaArtistas = [artista.nome for artista in self.ctrlPrincipal.ctrlArtista.listaArtistas]
        if not listaArtistas:
            messagebox.showinfo("Erro", "Cadastre um artista primeiro!")
            return
        self.limiteIns = LimiteInsereAlbum(self, listaArtistas)

    def addFaixaHandler(self, event):
        titulo = self.limiteIns.inputFaixa.get()
        nroFaixa = self.limiteIns.inputNroFaixa.get()
        if titulo and nroFaixa:
            musica = Musica(titulo, nroFaixa)
            self.listaFaixasTemp.append(musica)
            self.limiteIns.mostraJanela('Sucesso', f'Faixa "{titulo}" adicionada.')
            self.limiteIns.inputFaixa.delete(0, tk.END)
            self.limiteIns.inputNroFaixa.delete(0, tk.END)
        else:
            self.limiteIns.mostraJanela('Erro', 'Preencha o título e o número da faixa.')

    def criaAlbumHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        ano = self.limiteIns.inputAno.get()
        escolha = self.limiteIns.escolhaArtista.get()
        if escolha == "Vários artistas":
            indices = self.limiteIns.listboxArtistas.curselection()
            artistas = [self.ctrlPrincipal.ctrlArtista.listaArtistas[i] for i in indices]
            nomeArtista = "Vários artistas"
        else:
            artistas = [self.ctrlPrincipal.ctrlArtista.getArtista(escolha)]
            nomeArtista = escolha
        indicesMusicas = self.limiteIns.listboxMusicas.curselection()
        if not (titulo and ano and artistas and indicesMusicas):
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos e selecione pelo menos uma música.')
            return
        album = Album(titulo, nomeArtista, ano)
        for idx in indicesMusicas:
            texto = self.limiteIns.listboxMusicas.get(idx)
            nroFaixa, resto = texto.split('.', 1)
            tituloMusica = resto.split('(')[0].strip()
            artistaNome = resto.split('(')[1].replace(')', '').strip()
            artista = next((a for a in artistas if a.nome == artistaNome), None)
            if artista:
                musica = next((m for m in artista.musicas if m.titulo == tituloMusica and m.nroFaixa == nroFaixa), None)
                if musica:
                    album.adiciona_faixa(musica)
        self.listaAlbuns.append(album)
        for artista in artistas:
            artista.adiciona_album(album)
        self.limiteIns.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso!')

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaAlbum(self):
        self.limiteConsulta = LimiteConsultaAlbum(self, [album.titulo for album in self.listaAlbuns])

    def consultaHandler(self, event):
        titulo = self.limiteConsulta.inputTitulo.get()
        album = self.getAlbum(titulo)
        if album:
            msg = f"Álbum: {album.titulo} ({album.ano})\nArtista: {album.artista.nome}\nFaixas:\n"
            for faixa in album.faixas:
                msg += f"{faixa.nroFaixa}. {faixa.titulo}\n"
        else:
            msg = "Álbum não encontrado."
        self.limiteConsulta.mostraJanela('Consulta Álbum', msg)

    def fechaHandlerConsulta(self, event):
        self.limiteConsulta.destroy()