# GO2COD_PY_02
# By Kena Fayera
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com/") # This website allows scraping the data.
soup = BeautifulSoup(page_to_scrape.text,"html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote,author in zip(quotes,authors):
    print(quote.text + " - " + author.text)