import tkinter as tk
from tkinter import ttk, messagebox

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas

    def adiciona_musica(self, musica):
        self.__musicas.append(musica)

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x350')
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text = "Nome da playlist: ")
        self.labelNome.pack(side = "left")
        self.inputNome = tk.Entry(self.frameNome, width = 30)
        self.inputNome.pack(side = "left")

        self.labelArtista = tk.Label(self.frameArtista, text = "Selecione o artista: ")
        self.labelArtista.pack(side = "left")
        self.escolhaArtista = tk.StringVar()
        self.comboboxArtista = ttk.Combobox(self.frameArtista, width = 25, textvariable = self.escolhaArtista)
        self.comboboxArtista.pack(side = "left")
        self.comboboxArtista['values'] = listaArtistas
        self.comboboxArtista.bind("<<ComboboxSelected>>", controle.atualizaMusicas)

        self.labelMusica = tk.Label(self.frameMusica, text = "Selecione a música: ")
        self.labelMusica.pack(side = "left")
        self.listboxMusicas = tk.Listbox(self.frameMusica, width = 30)
        self.listboxMusicas.pack(side = "left")

        self.buttonAddMusica = tk.Button(self.frameButton, text = "Adicionar Música")
        self.buttonAddMusica.pack(side = "left")
        self.buttonAddMusica.bind("<Button>", controle.addMusicaHandler)

        self.buttonCria = tk.Button(self.frameButton, text = "Cadastrar Playlist")
        self.buttonCria.pack(side = "left")
        self.buttonCria.bind("<Button>", controle.criaPlaylistHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle, listaPlaylists):
        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consultar Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text = "Nome da playlist: ")
        self.labelNome.pack(side = "left")
        self.inputNome = tk.Entry(self.frameNome, width = 25)
        self.inputNome.pack(side = "left")

        self.buttonConsulta = tk.Button(self.frameButton, text = "Consultar")
        self.buttonConsulta.pack(side = "left")
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text = "Fechar")
        self.buttonFecha.pack(side = "left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlPlaylist:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.listaPlaylists = []
        self.musicasTemp = []

    def inserePlaylist(self):
        listaArtistas = [artista.nome for artista in self.ctrlPrincipal.ctrlArtista.listaArtistas]
        if not listaArtistas:
            messagebox.showinfo("Erro", "Cadastre um artista primeiro!")
            return
        self.musicasTemp = []
        self.limiteIns = LimiteInserePlaylist(self, listaArtistas)

    def atualizaMusicas(self, event):
        nomeArtista = self.limiteIns.escolhaArtista.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArtista)
        self.limiteIns.listboxMusicas.delete(0, tk.END)
        if artista:
            musicas = []
            for album in artista.albuns:
                for musica in album.faixas:
                    musicas.append(f"{musica.nroFaixa}. {musica.titulo} ({album.titulo})")
            for m in musicas:
                self.limiteIns.listboxMusicas.insert(tk.END, m)

    def addMusicaHandler(self, event):
        idx = self.limiteIns.listboxMusicas.curselection()
        if not idx:
            self.limiteIns.mostraJanela('Erro', 'Selecione uma música.')
            return
        nomeArtista = self.limiteIns.escolhaArtista.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArtista)
        if artista:
            selecionado = self.limiteIns.listboxMusicas.get(idx[0])
            nroFaixa, resto = selecionado.split('.', 1)
            tituloMusica = resto.split('(')[0].strip()
            for album in artista.albuns:
                for musica in album.faixas:
                    if musica.titulo == tituloMusica and musica.nroFaixa == nroFaixa:
                        self.musicasTemp.append(musica)
                        self.limiteIns.mostraJanela('Sucesso', f'Música "{musica.titulo}" adicionada.')
                        self.limiteIns.listboxMusicas.delete(idx[0])
                        return

    def criaPlaylistHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        if not (nome and self.musicasTemp):
            self.limiteIns.mostraJanela('Erro', 'Preencha o nome e adicione pelo menos uma música.')
            return
        playlist = Playlist(nome)
        for musica in self.musicasTemp:
            playlist.adiciona_musica(musica)
        self.listaPlaylists.append(playlist)
        self.limiteIns.mostraJanela('Sucesso', 'Playlist cadastrada com sucesso!')

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaPlaylist(self):
        self.limiteConsulta = LimiteConsultaPlaylist(self, [pl.nome for pl in self.listaPlaylists])

    def consultaHandler(self, event):
        nome = self.limiteConsulta.inputNome.get()
        playlist = None
        for pl in self.listaPlaylists:
            if pl.nome.lower() == nome.lower():
                playlist = pl
                break
        if playlist:
            msg = f"Playlist: {playlist.nome}\nMúsicas:\n"
            for musica in playlist.musicas:
                msg += f"{musica.nroFaixa}. {musica.titulo}\n"
        else:
            msg = "Playlist não encontrada."
        self.limiteConsulta.mostraJanela('Consulta Playlist', msg)

    def fechaHandlerConsulta(self, event):
        self.limiteConsulta.destroy()