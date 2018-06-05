import os
import telepot

# Credenciais API Spotify
os.environ['SPOTIPY_CLIENT_ID']='seu-client-id'
os.environ['SPOTIPY_CLIENT_SECRET']='seu-client-secret'
os.environ['SPOTIPY_REDIRECT_URI']='qualquer-uri-autorizada' # Veja sua Dashboard

# Token para o Bot do Telegram
os.environ['TELEGRAM_BOT_TOKEN'] = 'token-do-seu-bot'
