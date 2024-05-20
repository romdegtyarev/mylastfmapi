#!/usr/bin/env python3
"""
Show 20 last played tracks
"""
import json
import pylast

from conf import lastfm_network

def track_only(track):
    return f"{track.item}"

def get_top_tracks(username, number):
    print("get_top_tracks: Start")
    data_array = []
    full_data = {}
    top_tracks = lastfm_network.get_user(username).get_top_tracks(limit=number)
    for i, track in enumerate(top_tracks):
        printable = track_only(track)
        #print(str(i + 1) + " " + printable)
        data = {'name': printable}
        data_array.append(data)
    full_data["entry"] = data_array
    with open('./music/top.json', 'w') as json_file:
        json.dump(full_data, json_file)
    return top_tracks


# End of file
