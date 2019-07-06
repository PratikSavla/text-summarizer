import requests
import pandas as pd    
def Topnews():
   # BBC news api
   my_api_key="aeefa9bd8c274ed091810a3c5bf4d2d8"
   my_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="+my_api_key
   my_open_bbc_page = requests.get(my_url).json()
   my_article = my_open_bbc_page["articles"]
   my_results = []
   for ar in my_article:
      my_results.append(ar["title"])
      print(ar)
      break
   #for i in range(len(my_results)):
   #   print(i + 1, my_results[i])
   #   break
   print(my_open_bbc_page)
# Driver Code
if __name__ == '__main__':
   # function call
   Topnews()