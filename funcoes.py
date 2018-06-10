# -*- coding: utf-8 -*-

import spotipy
import simplejson as json
from spotipy.oauth2 import SpotifyClientCredentials
from fuzzywuzzy import fuzz

from formatos import *

from dotenv import load_dotenv, find_dotenv
load_dotenv('credenciais.env')

client_credentials_manager = SpotifyClientCredentials()

def lancamentos():

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.new_releases(limit=10)

    if retornoSpotipy:
        albums = retornoSpotipy['albums']
        return internacionais.format(showItensEnumerados(albums['items']))

    return erroPadrao

def similar(nome):

    artista = procuraArtista(nome)
    musica = procuraMusica(nome)

    if musica and artista and fuzz.ratio(nome,musica['name']) <= fuzz.ratio(nome,artista['name']):
        musica = None

    if musica:
        return recomendacoesMusica(musica)
    if artista:
        return recomendacoesArtista(artista)

    return erroBusca.format(nome)

def procuraMusica(nome):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.search(q='track:' + nome, type='track')
    items = retornoSpotipy['tracks']['items']

    if len(items) > 0:
        return items[0]

    return None

def procuraArtista(nome):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.search(q='artist:' + nome, type='artist')
    items = retornoSpotipy['artists']['items']

    if len(items) > 0:
        return items[0]

    return None

def recomendacoesArtista(artista):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.recommendations(seed_artists = [artista['id']],limit=10)

    if retornoSpotipy:
        return recomendacoes.format(artista['name'],showItens(retornoSpotipy['tracks']))

    return erroPadrao


def recomendacoesMusica(musica):

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    retornoSpotipy = sp.recommendations(seed_tracks = [musica['id']],limit=10)

    if retornoSpotipy:
        return recomendacoes.format(showItem(musica),showItens(retornoSpotipy['tracks']))

    return erroPadrao
