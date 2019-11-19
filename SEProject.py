from newsapi import NewsApiClient
import requests
import spotipy
import spotipy.oauth2 as oauth2
import random
import nltk
from nltk.corpus import words
import tkinter

m=tkinter.Tk()
m.title("Track Recommendation Application")

top_frame= tkinter.Frame(m).pack()
bottom_frame = tkinter.Frame(m).pack(side="bottom")

tkinter.Label(m, text = "This application generates track recommendations from Spotify, based on today's news.", fg="white", bg="red").pack(fill="x")

btn1 = tkinter.Button(top_frame, text = "Generate Recommendations", fg="green").pack()

## Retrieve top headlines and append to list.
def TopHeadlines():
    news_URL = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=108a2d7663e94e639f96a3a6c77d82f1"
    open_page = requests.get(news_URL).json()
    article = open_page["articles"]
    headlines = []
    for i in article:
        headlines.append(i["title"])
    for j in range (len(headlines)):
        return headlines
    
Headlines = TopHeadlines()

## if word in list is longer than 5 characters
## then append to data
Headlines1 = "".join(Headlines)
processedData = ' '.join([w for w in Headlines1.split() if len(w)>5])
data = processedData.split()

## Download word dictionary
nltk.download('words')
## Check if word is in english dictionary and append to new list
newdata = []
for i in data:
    if i in words.words():
        newdata.append(i)

## Choose random word from list
Random_News_Word = random.choice(newdata)

print("")
print("Headlines: ", Headlines)
print("")
print ("Key Word: ", Random_News_Word)
print("")

## Spotify Authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id="c367030cba0547c18102ec491320e635",
        client_secret="3286485fbcca41f7b324a6602221755e")

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

## Search spotify for keyword extracted from headlines
##returns 20 tracks that are based on the 'Random_News_Word'
results = sp.search(q=Random_News_Word, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print (' ', i, t['name'], ' - ', t['artists'] [0] ['name'])
    print(' ', i, t['album']['images'][0]['url'])
    print("")

m.mainloop()