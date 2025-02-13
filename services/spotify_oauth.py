import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "beef1f3d454240eab804424187d37bb6"
SPOTIFY_CLIENT_SECRET = "12ac03b8466240e5b15f053c42ce55c9"
SPOTIFY_REDIRECT_URI = "https://5000-grassigiova-spotysecond-i3w6w2glon4.ws-eu117.gitpod.io/callback"

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)

def get_spotify_object (token_info):
    return spotipy.Spotify(auth=token_info['access_token'])