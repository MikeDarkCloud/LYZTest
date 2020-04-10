import json

def getJsonParm(text,key):
    '''字符串转为字典'''
    ldict = json.loads(text,encoding='utf-8')
    return ldict[key]

def getJson(ldict):
    '''字典转为json'''
    ldict = json.dumps(ldict,ensure_ascii=False)
    return ldict





# print(getJsonParm(js,'payInfos')[0]['subOrderNo'])