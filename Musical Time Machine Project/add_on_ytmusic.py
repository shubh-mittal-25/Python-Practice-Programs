from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD :\n")
response = requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date}/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

top_100_list = [song.getText() for song in soup.find_all('h3' , class_='chart-entry__title')]
print(top_100_list)

yt = YTMusic("browser.json")

PLAYLIST_NAME = f"{date} Billboard 100"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

    # Search and add each song
    for song in top_100_list:
        try:
            search_results = yt.search(song, filter="songs", limit=1)
            yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
            print(f"Added: {song}")
        except Exception as e:
            print(f"Skipped: {song} | Reason: {e}")