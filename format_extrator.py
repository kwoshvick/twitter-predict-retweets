import csv
import json
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import multiprocessing
multiprocessing.set_start_method('forkserver')

def csvWriter(list):
    with open("data/sorted_csv.csv", 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list)

myJsonString = open('data/train.json')

headers = ['created_at','location','followers_count','friends_count',
           'listed_count','favourites_count','sentiment_class',
           'sentiment_pos','sentiment_neg','retweet_count']

jsonObjects = json.load(myJsonString)


def extractFromJson(jsonObjects):
    for jsonObject in jsonObjects:
        jsonList = list()
        jsonList.append(jsonObject['created_at'].replace("+0000 ",""))
        jsonList.append(jsonObject['user']['location'])
        jsonList.append(jsonObject['user']['followers_count'])
        jsonList.append(jsonObject['user']['friends_count'])
        jsonList.append(jsonObject['user']['listed_count'])
        jsonList.append(jsonObject['user']['favourites_count'])
        text = jsonObject['text']
        blob = TextBlob(text,analyzer=NaiveBayesAnalyzer())
        sentiment_values = blob.sentiment
        jsonList.append(sentiment_values[0]) #class
        jsonList.append(sentiment_values[1]) # pos
        jsonList.append(sentiment_values[2]) # negative
        jsonList.append(jsonObject['retweet_count'])
        csvWriter(jsonList)

if __name__ == '__main__':
    datasetCsv = 'data/sorted_dataset.csv'
    datasetJson = 'data/train.json'

    myJsonString = open(datasetJson)
    csvHeaders = ['created_at', 'location', 'followers_count', 'friends_count','listed_count', 'favourites_count']
    jsonObjects = json.load(myJsonString)

    with open("data/nb_csv.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        outfile.close()



