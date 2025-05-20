import os
from dotenv import load_dotenv
import pylast

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
USERNAME = os.getenv("USERNAME")
SPOTIFY_CID = os.getenv("SPOTIFY_CID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_PL_ID = os.getenv("SPOTIFY_PL_ID")

lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET
)

