import json

myJsonString = open('data/practise.json')
jsonObjects = json.load(myJsonString)


myFile = open('test2.json','w')
myFile.writelines('[')
jsonCounterPosition = 0

jsonObjectsSize = len(jsonObjects)

for jsonObject in jsonObjects:
    jsonCounterPosition += 1
    jsonDict = dict()
    jsonDict['created_at'] = jsonObject['created_at'].replace("+0000 ","")
    jsonDict['location'] = jsonObject['user']['location']
    jsonDict['followers_count'] = jsonObject['user']['followers_count']
    jsonDict['friends_count'] = jsonObject['user']['friends_count']
    jsonDict['listed_count'] = jsonObject['user']['listed_count']
    jsonDict['favourites_count'] = jsonObject['user']['favourites_count']
    jsonDict['retweet_count'] = jsonObject['retweet_count']
    jsonDict['text'] = jsonObject['text']

    myFile.write(json.dumps(jsonDict, indent=4))
    if(jsonCounterPosition < jsonObjectsSize):
        myFile.writelines(',')


myFile.writelines(']')
myFile.close()


