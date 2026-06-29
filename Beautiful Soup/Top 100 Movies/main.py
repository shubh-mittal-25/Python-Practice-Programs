from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
all_movies = soup.find_all('h3', class_='title')
movie_list = [item.getText() for item in all_movies]
movie_list.reverse()
with open('movies.txt', 'w', encoding="utf-8") as f:
    for movie in movie_list:
        f.write(f"{movie}\n")