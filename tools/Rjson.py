import json

def getJsonParm(text,key = None):
    '''字符串转为字典'''
    ldict = json.loads(text,encoding='utf-8')
    if key == None:
        return ldict
    if key != None:
        return ldict[key]

def getJson(ldict):
    '''字典转为json'''
    ldict = json.dumps(ldict,ensure_ascii=False)
    return ldict


def readDict(ldict:dict,key:tuple):
    if len(key) == 0 or len(key) >= 6:
        raise Exception("参数不能为空或参数超过5个！")
    if len(key) == 1:
        p = ldict[key[0]]
        return str(p)

    if len(key) == 2:
        p = ldict[key[0]][key[1]]
        return str(p)

    if len(key) == 3:
        p = ldict[key[0]][key[1]][key[2]]
        return str(p)

    if len(key) == 4:
        p = ldict[key[0]][key[1]][key[2]][key[3]]
        return str(p)

    if len(key) == 5:
        p = ldict[key[0]][key[1]][key[2]][key[3]][key[4]]
        return str(p)


# print(getJsonParm(js,'payInfos')[0]['subOrderNo'])