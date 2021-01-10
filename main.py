import pandas as pd
import requests
import json
import datetime

# Python files for ETL process
from extract import get_spotify_data
from transform import check_if_valid_data
from load import load_spotify_data

# def get_spotify_token():
#     headers = {
#         "Accept": "application/x-www-form-urlencoded",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#     data = {
#         'grant_type': 'refresh_token',
#         "refresh_token": TOKEN
#     }
#     token_refresh_url = "https://api.spotify.com/v1/refresh"
#     res = requests.post(token_refresh_url, headers = headers, auth = (CLIENT_ID, CLIENT_SECRET), data = data)
#     print(res)

if __name__ == "__main__":

    # EXTRACT
    songs_df = get_spotify_data()
    print(songs_df)
    
    # VALIDATE
    if check_if_valid_data(songs_df):
        print("\nValid data received\n")
    
    # LOAD
    load_spotify_data(songs_df)
