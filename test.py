import json

mydictionary = dict()
mydictionary2 = dict()

mydictionary['a'] = 1234561
mydictionary['b'] = 1234562
mydictionary['c'] = 1234563
mydictionary['d'] = 1234564
mydictionary['e'] = 1234565
mydictionary['f'] = 1234566
mydictionary['g'] = 1234567
mydictionary['h'] = 1234568
mydictionary['i'] = 1234569



mydictionary2['a'] = 1234561
mydictionary2['b'] = 1234562
mydictionary2['c'] = 1234563
mydictionary2['d'] = 1234564
mydictionary2['e'] = 1234565
mydictionary2['f'] = 1234566
mydictionary2['g'] = 1234567
mydictionary2['h'] = 1234568
mydictionary2['i'] = 1234569

mylist = list()

mylist.append(mydictionary)
mylist.append(mydictionary2)

print(json.dumps(mylist,indent=4))


# myFile = open('test.json','w')
# myFile.writelines('[')
# myFile.write(json.dumps(mydictionary,indent=4))
# myFile.writelines(',')
# myFile.write(json.dumps(mydictionary2,indent=4))
# myFile.writelines(']')
# print(json.dumps(mydictionary2,indent=4))
#
# myFile.close()
