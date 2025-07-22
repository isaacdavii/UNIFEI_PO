import os

from classes.album import Album
from classes.artista import Artista
# from classes.musica import Musica
from classes.facilidades import exibir_nome_do_programa, exibir_opcoes, escolher_opcao
# from classes.playlist import *

# Artistas
artista1 = Artista('Linkin Park')
artista2 = Artista('Coldplay')
artista3 = Artista('Imagine Dragons')

# Álbuns
album1 = Album('Hybrid Theory', 2000, artista1)
album2 = Album('Meteora', 2003, artista1)
album3 = Album('A Head Full of Dreams', 2015, artista2)
album4 = Album('Viva La Vida', 2008, artista2)
album5 = Album('Night Visions', 2012, artista3)
album6 = Album('Evolve', 2017, artista3)


# Músicas
# musica1 = Musica('In the end', 2000, artista1, album1)
# musica2 = Musica('One Step Closer', 2000, artista1, album1)
# musica3 = Musica('Papercut', 2000, artista1, album1)
# muisca4 = Musica('Numb', 2003, artista1, album2)
# musica5 = Musica('Breaking the Habit', 2003, artista1, album2)
# musica6 = Musica('Faint', 2003, artista1, album2)
# musica7 = Musica('Somewhere I Belong', 2003, artista1, album2)
# musica8 = Musica('A Sky Full of Stars', 2015, artista2, album3)
# musica9 = Musica('Adventure of a Lifetime', 2015, artista2, album3)
# musica10 = Musica('Viva La Vida', 2008, artista2, album4)
# musica11 = Musica('Paradise', 2011, artista2, album4)
# musica12 = Musica('Demons', 2012, artista3, album5)
# musica13 = Musica('Radioactive', 2012, artista3, album5)
# musica14 = Musica('Believer', 2017, artista3, album6)
# musica15 = Musica('Thunder', 2017, artista3, album6)

# album1.adicionarMusica(musica1)
# album1.adicionarMusica(musica2)
# album1.adicionarMusica(musica3)
# album2.adicionarMusica(muisca4)
# album2.adicionarMusica(musica5)
# album2.adicionarMusica(musica6)
# album2.adicionarMusica(musica7)
# album3.adicionarMusica(musica8)
# album3.adicionarMusica(musica9)
# album4.adicionarMusica(musica10)
# album5.adicionarMusica(musica11)
# album5.adicionarMusica(musica12)
# album6.adicionarMusica(musica13)
# album6.adicionarMusica(musica14)
# album6.adicionarMusica(musica15)


# playlist1 = Playlist('Rock')
# playlist1.adicionarMusica(musica1)
# playlist1.adicionarMusica(musica2)

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()