import tkinter as tk
from tkinter import messagebox, ttk

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

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    @property
    def albuns(self):
        return self.__albuns
    @property
    def musicas(self):
        return self.__musicas
    
    def adiciona_musica(self, musica):
        self.__musicas.append(musica)
        
    def adiciona_album(self, album):
        self.__albuns.append(album)

class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text = "Nome do artista: ")
        self.labelNome.pack(side = "left")
        self.inputNome = tk.Entry(self.frameNome, width = 20)
        self.inputNome.pack(side = "left")

        self.buttonSubmit = tk.Button(self.frameButton, text = "Cadastrar")
        self.buttonSubmit.pack(side = "left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereMusicaArtista(tk.Toplevel):
    def __init__(self, controle, artista):
        tk.Toplevel.__init__(self)
        self.geometry('250x120')
        self.title(f"Cadastrar Música para {artista.nome}")
        self.controle = controle
        self.artista = artista

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
        self.buttonSubmit.bind("<Button>", lambda e: controle.enterMusicaHandler(e, artista))

        self.buttonFecha = tk.Button(self.frameButton, text = "Concluído")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaMusicaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Consultar Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text = "Nome do artista: ")
        self.labelNome.pack(side = "left")
        self.inputNome = tk.Entry(self.frameNome, width = 20)
        self.inputNome.pack(side = "left")

        self.buttonConsulta = tk.Button(self.frameButton, text = "Consultar")
        self.buttonConsulta.pack(side = "left")
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista:
    def __init__(self):
        self.listaArtistas = [
            Artista("Linkin Park"),
            Artista("Nirvana"),
            Artista("Eminem")
        ]

    def getArtista(self, nome):
        for artista in self.listaArtistas:
            if artista.nome.lower() == nome.lower():
                return artista
        return None

    def insereArtista(self):
        self.limiteIns = LimiteInsereArtista(self)

    def consultaArtista(self):
        self.limiteConsulta = LimiteConsultaArtista(self)
        
    def insereMusicaArtista(self):
        # Seleciona artista
        nomes = [a.nome for a in self.listaArtistas]
        if not nomes:
            messagebox.showinfo("Erro", "Cadastre um artista primeiro!")
            return
    
        # Janela para escolher artista
        self.limiteSel = tk.Toplevel()
        self.limiteSel.geometry('250x100')
        self.limiteSel.title("Selecionar Artista")
        tk.Label(self.limiteSel, text = "Escolha o artista:").pack()
        self.combo = ttk.Combobox(self.limiteSel, values = nomes)
        self.combo.pack()
        tk.Button(self.limiteSel, text = "OK", command = self.abrirCadastroMusica).pack()

    def abrirCadastroMusica(self):
        nome = self.combo.get()
        artista = self.getArtista(nome)
        self.limiteSel.destroy()
        self.limiteMusica = LimiteInsereMusicaArtista(self, artista)

    def enterMusicaHandler(self, event, artista):
        titulo = self.limiteMusica.inputTitulo.get()
        nroFaixa = self.limiteMusica.inputFaixa.get()
        if not (titulo and nroFaixa):
            self.limiteMusica.mostraJanela('Erro', 'Preencha todos os campos!')
            return
        for m in artista.musicas:
            if m.titulo.lower() == titulo.lower():
                self.limiteMusica.mostraJanela('Erro', 'Música já cadastrada!')
                return
        musica = Musica(titulo, nroFaixa)
        artista.adiciona_musica(musica)
        self.limiteMusica.mostraJanela('Sucesso', 'Música cadastrada com sucesso!')
        self.limiteMusica.inputTitulo.delete(0, tk.END)
        self.limiteMusica.inputFaixa.delete(0, tk.END)

    def fechaMusicaHandler(self, event):
        self.limiteMusica.destroy()
        

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        if self.getArtista(nome):
            self.limiteIns.mostraJanela('Erro', 'Artista já cadastrado!')
        else:
            artista = Artista(nome)
            self.listaArtistas.append(artista)
            self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso!')
        self.limiteIns.inputNome.delete(0, tk.END)

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaHandler(self, event):
        nome = self.limiteConsulta.inputNome.get()
        artista = self.getArtista(nome)
        
        if artista:
            msg = f"Álbuns de {artista.nome}:\n"
            if artista.albuns:
                for album in artista.albuns:
                    msg += f"- {album.titulo} ({album.ano})\n"
                    for musica in album.faixas:
                        msg += f"   {musica.nroFaixa}. {musica.titulo}\n"
            else:
                msg += "Nenhum álbum cadastrado."
        else:
            msg = "Artista não encontrado."
        self.limiteConsulta.mostraJanela('Consulta Artista', msg)

    def fechaHandlerConsulta(self, event):
        self.limiteConsulta.destroy()