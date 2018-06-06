def showArtistas(artists):
    resposta = ""
    for j, artist in enumerate(artists):
        resposta += artist['name']

        if (j < len(artists) - 2):
            resposta += ", "
        elif (j == len(artists) - 2):
            resposta += " e "
    return resposta

def showAlbum(album):
    return '_' + album['name'] + "_ - " + showArtistas(album['artists'])

def showAlbums(albums):
    resposta = ""
    for i, album in enumerate(albums):
        resposta += "#" + str(i+1) + ": " + showAlbum(album) + "\n\n"
    return resposta

def showMusica(musica):
    return '_' + musica['name'] + "_ - " + showArtistas(musica['artists'])

def showMusicas(musicas):
    resposta = ""
    for musica in musicas:
        resposta += showMusica(musica) + "\n\n"
    return resposta
