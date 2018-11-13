import csv
import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

jsonDict = dict()
finalDict = dict()
location = list()
followers_count = list()
friends_count = list()
listed_count = list()
favourites_count = list()
favorite_count = list()
sentiment_class = list()
sentiment_pos = list()
sentiment_neg = list()

myjson = pd.read_json('data/train.json')
for data in myjson:
    jsonDict[data] = list(myjson[data])


for userData in jsonDict['user']:
    location.append(userData['location'])
    followers_count.append(userData['followers_count'])
    friends_count.append(userData['friends_count'])
    listed_count.append(userData['listed_count'])
    favourites_count.append(userData['favourites_count'])

finalDict['followers_count'] = followers_count
finalDict['friends_count'] = friends_count
finalDict['listed_count'] = listed_count
finalDict['favourites_count'] = favourites_count
finalDict['favorite_count'] = favorite_count
finalDict['favorite_count'] = jsonDict['favorite_count']

for text in  jsonDict['text']:
    blob = TextBlob(text,analyzer=NaiveBayesAnalyzer())
    sentiment_values = blob.sentiment
    sentiment_class.append(sentiment_values[0])
    sentiment_pos.append(sentiment_values[1])
    sentiment_neg.append(sentiment_values[2])

finalDict['sentiment_class'] = sentiment_class
finalDict['sentiment_pos'] = sentiment_pos
finalDict['sentiment_neg'] = sentiment_neg

finalDict['created_at'] = jsonDict['created_at']
finalDict['retweet_count'] = jsonDict['retweet_count']

keys = sorted(finalDict.keys())
with open("sorted_csv.csv", "w") as outfile:
   writer = csv.writer(outfile, delimiter = "\t")
   writer.writerow(keys)
   writer.writerows(zip(*[finalDict[key] for key in keys]))











