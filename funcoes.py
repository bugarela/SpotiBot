# -*- coding: utf-8 -*-

import spotipy
import simplejson as json
from spotipy.oauth2 import SpotifyClientCredentials
from fuzzywuzzy import fuzz

import formatos

from dotenv import load_dotenv, find_dotenv
load_dotenv('credenciais.env')

client_credentials_manager = SpotifyClientCredentials()

def lancamentos():

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.new_releases(limit=10)

    resposta = "Últimos lançamentos internacionais:\n\n"

    if retornoSpotipy:
        albums = retornoSpotipy['albums']
        resposta += formatos.showAlbums(albums['items'])

    else:
        resposta = "Oops, algo deu errado :("

    return resposta

def similar(nome):

    artista = procuraArtista(nome)
    musica = procuraMusica(nome)

    if musica and artista and fuzz.ratio(nome,musica['name']) <= fuzz.ratio(nome,artista['name']):
        musica = None

    if musica:
        return recomendacoesMusica(musica)
    elif artista:
        return recomendacoesArtista(artista)
    else:
        return "Não encontrei esse artista :("

def procuraMusica(nome):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.search(q='track:' + nome, type='track')
    items = retornoSpotipy['tracks']['items']

    if len(items) > 0:
        return items[0]
    else:
        return None

def procuraArtista(nome):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.search(q='artist:' + nome, type='artist')
    items = retornoSpotipy['artists']['items']

    if len(items) > 0:
        return items[0]
    else:
        return None

def recomendacoesArtista(artista):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.recommendations(seed_artists = [artista['id']],limit=10)

    if retornoSpotipy:
        resposta = "Recomendações para quem gosta de " + artista['name'] + ":\n\n"
        resposta += formatos.showMusicas(retornoSpotipy['tracks'])
    else:
        resposta = "Oops, algo deu errado :("

    return resposta

def recomendacoesMusica(musica):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.recommendations(seed_tracks = [musica['id']],limit=10)

    if retornoSpotipy:
        resposta = "Recomendações para quem gosta de " + formatos.showMusica(musica) + ":\n\n"
        resposta += formatos.showMusicas(retornoSpotipy['tracks'])
    else:
        resposta = "Oops, algo deu errado :("

    return resposta
