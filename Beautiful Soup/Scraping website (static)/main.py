from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all("a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all("span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)