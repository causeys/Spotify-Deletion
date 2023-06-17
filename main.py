import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secret import client_id, client_secret, playlist_id

# Login to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://localhost",
                                               scope="playlist-modify-public"))

# Prompt user for artist name to delete
name = input("Enter artist name: ")
if len(name) >= 1:
    name = name
else:
    name = "Rick Astley"

artist_search = sp.search(q='artist:' + name, type='artist')
items = artist_search['artists']['items']
if len(items) > 0:
    artist = items[0]
    artist_uri = artist['uri']



# Enter spotify playlist id into secret.py file
# Search for songs to be deleted within playlist
results = sp.playlist_items(playlist_id)
track_list = []
for item in (results['items']):
    track = item['track']
    if track['artists'][0]['uri'] == artist_uri:
        track_id = track['id']
        track_list.append(track_id)


# Remove list of songs from playlist
new_playlist = sp.playlist_remove_all_occurrences_of_items(playlist_id, track_list)
print("All done!")
