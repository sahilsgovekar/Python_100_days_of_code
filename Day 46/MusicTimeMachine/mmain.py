
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = "8f75bf34cb7c4b27b9afba38e767b255"
client_secret = "52b1e5d8d184414eb7c3a10697c2af80"

date_input = input("Which date you want to travel \nEnter in yyyy-mm-dd format :")
# date_list = date_input.split("-")
# year = int(date_list[0])
# mont = int(date_list[1])
# day = int(date_list[2])
# reesponse  = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")

song_names_list = ["Sorry", "Take me there"]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
webdata = response.text

soup  = BeautifulSoup(webdata, "html.parser")
songs = soup.select(selector="li h3")
song_names_list_nofilter = [song.getText().replace('\n\n\t\n\t\n\t\t\n\t\t\t\t\t', '').replace('\t\t\n\t\n', '') for song in songs]
song_names_list = song_names_list_nofilter[0:99]
# print(song_names_list)



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]