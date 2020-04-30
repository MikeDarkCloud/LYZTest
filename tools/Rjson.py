import json

def getJsonParm(text,key = None):
    '''字符串转为字典'''
    ldict = json.loads(text,encoding='utf-8')
    if key == None:
        return ldict
    if key != None:
        return ldict[key]

def getJson(ldict:dict):
    '''字典转为json'''
    ldict = json.dumps(ldict,ensure_ascii=False)
    return ldict


def readDict(ldict:dict, keys:tuple):
    '''读取字典的值'''
    if len(keys) == 0 or len(keys) >= 6:
        raise Exception("参数不能为空或参数超过5个！")
    if len(keys) == 1:
        p = ldict[keys[0]]
        return str(p)

    if len(keys) == 2:
        p = ldict[keys[0]][keys[1]]
        return str(p)

    if len(keys) == 3:
        p = ldict[keys[0]][keys[1]][keys[2]]
        return str(p)

    if len(keys) == 4:
        p = ldict[keys[0]][keys[1]][keys[2]][keys[3]]
        return str(p)

    if len(keys) == 5:
        p = ldict[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]
        return str(p)


# print(getJsonParm(js,'payInfos')[0]['subOrderNo'])