from classes.artista import Artista

class Musica:
    
    def __init__(self, titulo, ano, artista, album):
        print(f'Criando música: {titulo}')
        self._titulo = titulo
        self._ano = ano
        self._artista = artista
        self._album = album
        artista.adicionarMusica(self)
        if hasattr(album, 'adicionarMusica'):
            album.adicionarMusica(self)
        
    @property
    def titulo(self):
        return self._titulo
    @property
    def ano(self):
        return self._ano
    @property
    def artista(self):
        return self._artista
    @property
    def album(self):
        return self._album