import os

from classes.artista import Artista
from classes.album import Album
from classes.musica import Musica
from classes.playlist import Playlist

def menu():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
def exibir_nome_do_programa():
    print("""
Spotipobre - O Spotify do Pobre
    """)

def exibir_opcoes():
    print('1. Exibir artistas')
    print('2. Exibir playlists')
    print('3. Sair\n')
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            exibir_artistas()
        elif opcao_escolhida == 2:
            exibir_playlists()
        elif opcao_escolhida == 3:
            finalizar_app()
    
    except ValueError:
        opcao_invalida()
        
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal.\n')
    menu()
    
def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()
    
def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo!')

def exibir_artistas():
    exibir_subtitulo('LISTANDO ARTISTAS')
    
    for artista in Artista.artistas:
        print(f'Artista: {artista.nome}')
        print(f'Músicas: {len(artista.musicas)}')
        print(f'Álbuns: {len(artista.albuns)}')
        print()
    
    voltar_ao_menu_principal()

def exibir_playlists():
    exibir_subtitulo('LISTANDO PLAYLISTS')
    
    for playlist in Playlist.playlists:
        print(f'Playlist: {playlist.nome}')
        print(f'Músicas: {len(playlist.musicas)}')
        print()
    
    voltar_ao_menu_principal()


    

    
