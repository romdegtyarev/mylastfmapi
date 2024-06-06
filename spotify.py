import json
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import conf


cid = conf.SPOTIFY_CID
client_secret = conf.SPOTIFY_SECRET
pl_id = conf.SPOTIFY_PL_ID


auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


offset = 0
while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.name,items.track.artists.name,total',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break
    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])

