import os
import sys

import pylast


API_KEY = ""
API_SECRET = ""
USERNAME = ""
SPOTIFY_CID = ''
SPOTIFY_SECRET = ''
SPOTIFY_PL_ID = 'spotify:playlist:<id>'


lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET
)


# End of file
