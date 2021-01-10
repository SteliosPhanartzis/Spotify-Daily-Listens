import datetime
import pandas as pd
from secrets import SPOTIFY_TOKEN
import requests
import json

def get_spotify_data():
    # Request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=SPOTIFY_TOKEN)
    }

    # Variables to be used for request
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    spotify_url = "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp)

    # Stores response as json object
    data = requests.get(spotify_url, headers = headers).json()
    
    # Lists to store extracted data
    song_names = []
    artist_names = []
    played_at = []
    timestamps = []

    # Extracting only relevant data from json response 
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
    
    # Create dictionary from lists to turn into pandas dataframe
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at,
        "timestamp": timestamps
    }
    
    # Pandas dataframe creation
    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    return song_df