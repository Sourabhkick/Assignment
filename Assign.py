
import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com//cricket-news//126624//it-just-didnt-click-it-wasnt-meant-to-be-bangar-on-karthiks-downturn"
response = requests.get(url)

htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

Heading = []
News = []


heading = soup.find('h1', attrs={'class': 'nws-dtl-hdln'}).string
# Heading.append(heading)
print(heading)

unique_heading = set(heading.split())
print(unique_heading )
heading_count = len(heading.split())
print(heading_count)


for data in soup.find_all('p', attrs={'class': 'cb-nws-para'}):
 news = data.get_text()
# news = d.find('p', attrs={'class': 'cb-nws-para'}).get_text
# print(news)
unique_news = set(news.split())
print(unique_news)
news_count = len(news.split())
print(news_count)
