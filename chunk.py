import json
with open('data/train.json') as infile:
  o = json.load(infile)
  chunkSize = 1000
  for i in range(0, len(o), chunkSize):
    with open('chunks/file_' + str(i//chunkSize) + '.json', 'w') as outfile:
      json.dump(o[i:i+chunkSize], outfile, indent=4)