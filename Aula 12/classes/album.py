from classes.artista import Artista
from classes.musica import Musica

class Album:
    
    def __init__(self, titulo, ano, artista):
        print(f"Criando álbum: {titulo}, Ano: {ano}, Artista: {artista.nome}")
        self._titulo = titulo
        self._ano = ano
        self._artista = artista
        self._musicas = []
        artista.adicionarAlbum(self)
        
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
    def musicas(self):
        return self._musicas
    
    def adicionarMusica(self, musica):
        if isinstance(musica, Musica):
            self._musicas.append(musica)
        else: 
            raise TypeError('O objeto não é uma música')
            
    def adicionarArtista(self, artista):
        if isinstance(artista, Artista):
            self._artista.adicionarAlbum(artista)
        else:
            raise TypeError('O objeto não é um artista')
    
    def listarMusicas(self):
        print(f'Álbuns do artista {self._artista.nome}')
        for musica in self._musicas:
            print(f' - {musica.titulo} ({musica.ano})')