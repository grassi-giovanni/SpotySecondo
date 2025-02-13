import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "9214bb00011c4ac88e9abb2b6ce04ae1"
SPOTIFY_CLIENT_SECRET = "9412f99b5b05479ba88d0e6fa06d3afd"
SPOTIFY_REDIRECT_URI = "https://5000-iginiomassa-progettinos-06ic5e6lh2t.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui

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