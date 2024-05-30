import spotipy
from spotipy.oauth2 import SpotifyOAuth


def spotify_begining():
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a2656aab5a0f45d1b73d45d80f8cf09d",
												client_secret="a5ad97e3877b454cae5bc1f75ce1b450",
												redirect_uri="http://localhost:1234",
												scope="user-library-read user-modify-playback-state user-read-playback-state"))

	dillaz_uri = 'spotify:artist:15p1isN7VcGsjeSq8s9YeP'

	results = sp.artist_albums(dillaz_uri, album_type='album')
	albums = results['items']
	while results['next']:
		results = sp.next(results)
		albums.extend(results['items'])

	albums = albums[:1]
	devices = sp.devices()
	device_id = devices["devices"][0]["id"]

	for album in albums:
		album_id = album["id"]
		tracks = sp.album_tracks(album_id)
		tracks = tracks["items"]
		tracks = tracks[6:]
		for track in tracks:
			print(track["name"])
			track_uri = track["uri"]
			#sp.start_playback(device_id=device_id, uris=[track_uri])