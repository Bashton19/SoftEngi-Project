from newsapi import NewsApiClient
import pandas as pd
import requests
import spotipy




def TopHeadlines():
    news_URL = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=108a2d7663e94e639f96a3a6c77d82f1"
    open_page = requests.get(news_URL).json()
    article = open_page["articles"]
    headlines = []
    for i in article:
        headlines.append(i["title"])
    for j in range (len(headlines)):
        return headlines
    data = TopHeadlines()
    print (data)
    
Headlines = TopHeadlines()


print (Headlines)


