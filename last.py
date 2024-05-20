#!/usr/bin/env python3
"""
Show 20 last played tracks
"""
import json
import pylast

from conf import lastfm_network

def track_and_timestamp(track):
    return f"{track.playback_date}\t{track.track}"

def get_recent_tracks(username, number):
    print("get_recent_tracks: Start")
    data_array = []
    full_data = {}
    recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit=number)
    for i, track in enumerate(recent_tracks):
        printable = track_and_timestamp(track)
        #print(str(i + 1) + " " + printable)
        data = {'name': printable}
        data_array.append(data)
    full_data["entry"] = data_array
    with open('./music/last.json', 'w') as json_file:
        json.dump(full_data, json_file)
    return recent_tracks


# End of file
