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
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

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