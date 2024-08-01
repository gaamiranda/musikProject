import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tkinter import messagebox

def spoti_play(uri):

	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
												client_secret="",
												redirect_uri="http://localhost:1234",
												scope="user-library-read user-modify-playback-state user-read-playback-state"))

	devices = sp.devices()
	try:
		device_id = devices["devices"][0]["id"]
	except:
		messagebox.showerror("Erro", "No devices were found the program will close!")
		exit()

	sp.start_playback(device_id=device_id, uris=[uri])

def spoti_pause():
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
												client_secret="",
												redirect_uri="http://localhost:1234",
												scope="user-library-read user-modify-playback-state user-read-playback-state"))

	devices = sp.devices()
	try:
		device_id = devices["devices"][0]["id"]
	except:
		messagebox.showerror("Erro", "No devices were found the program will close!")
		exit()

	sp.pause_playback(device_id=device_id)

def spoti_resume():
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
												client_secret="",
												redirect_uri="http://localhost:1234",
												scope="user-library-read user-modify-playback-state user-read-playback-state"))

	devices = sp.devices()
	try:
		device_id = devices["devices"][0]["id"]
	except:
		messagebox.showerror("Erro", "No devices were found the program will close!")
		exit()

	sp.start_playback(device_id=device_id)

def get_artist_name(uri):
	pass
