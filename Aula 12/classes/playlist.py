class Playlist:
    playlists = []
    
    def __init__(self, nome):
        self._nome = nome
        self._musicas = []

    @property
    def nome(self):
        return self._nome
    @property
    def musicas(self):
        return self._musicas
    
    def adicionarMusica(self, musica):
        self._musicas.append(musica)