from newsapi import NewsApiClient
import pandas as pd
import requests
import spotipy
import spotipy.outh2 as oauth2
import sys



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


credentials = oauth2.SpotifyClientCredentials(
        client_id="c367030cba0547c18102ec491320e635",
        client_secret="3286485fbcca41f7b324a6602221755e")

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


#spotify = spotipy.Spotify()

#if len(sys.argv) > 1:
#    name = ' '.join(sys.argv[1:])
#else:
#    name = 'Space*'

#results = spotify.search(q='artist:' + name, type='artist')
#items = results['artists']['items']
#if len(items) > 0:
#    artist = items[0]
#    print (artist['name'], artist['images'][0]['url'])