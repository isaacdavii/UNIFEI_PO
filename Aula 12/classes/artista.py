class Artista:
    artistas = []
    
    def __init__(self, nome):
        print(f'Criando artista: {nome}')
        self._nome = nome
        self._musicas = []
        self._albuns = []
        Artista.artistas.append(self)
        
    @property
    def nome(self):
        return self._nome
    @property
    def musicas(self):
        return self._musicas
    @property
    def albuns(self):
        return self._albuns
    
    def adicionarMusica(self, musica):
        self._musicas.append(musica)
        
    def adicionarAlbum(self, album):
        self._albuns.append(album)
        
    