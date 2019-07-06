import requests
import pandas as pd    
from newspaper import Article

my_api_key="aeefa9bd8c274ed091810a3c5bf4d2d8"
my_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="+my_api_key
my_open_bbc_page = requests.get(my_url).json()
my_article = my_open_bbc_page["articles"]
my_results = []

for ar in my_article:
  url = (ar["url"])
  summary = ar["description"]
  print(summary)