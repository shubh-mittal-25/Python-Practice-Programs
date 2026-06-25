from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
article_title = soup.find("a", class_="storylink").getText()
print(article_title)