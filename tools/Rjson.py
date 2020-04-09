import json

def getJsonParm(text,key):
    ldict = json.loads(text)
    return ldict[key]



# print(getJsonParm(js,'payInfos')[0]['subOrderNo'])