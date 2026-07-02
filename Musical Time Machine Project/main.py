from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD :\n")
response = requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date}/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

top_100_list = [song.getText() for song in soup.find_all('h3' , class_='chart-entry__title')]


print(top_100_list)