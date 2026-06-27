from bs4 import BeautifulSoup
import requests

from Games.Higher_Lower import art

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    anchor = article_tag.find("a")
    text = anchor.getText()
    article_texts.append(text)
    link = anchor.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

most_upvotes = max(article_upvotes)
index = article_upvotes.index(most_upvotes)

print(f"""
Article with most upvotes :
{article_texts[index]}
{article_links[index]}
{article_upvotes[index]}
""")