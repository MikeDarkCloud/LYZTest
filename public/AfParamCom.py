import random
from tools.Rjson import *
from public.DataExtraction import *
class AfParamCom(DataExtraction):
    '''处理接口请求返回参数提取并保存'''
    def __init__(self):
        '''保存参数文件'''
        self.Yaml = 'LearnInfo'

    def saveParam(self,response,YamlFile,Ptuple:tuple):
        Result=DataExtraction().extRegxParam(response,YamlFile)
        param = Result[random.randint(0, len(Result) - 1)]
        if isinstance(param,tuple):
            for i in Ptuple:
                YamlParser(self.Yaml).setYaml(param[Ptuple.index(i)], (i,))
        else:
            YamlParser(self.Yaml).setYaml(param,(Ptuple,))


    def saveJson(self,response,key:tuple,Ptuple:tuple):
        jsonp = getJsonParm(response)
        for i in key:
            value = readDict(jsonp,i)
            YamlParser(self.Yaml).setYaml(str(value), (Ptuple[key.index(i)],))


    def moreParam(self,response,YamlFile,Ptuple:tuple):
        Result = DataExtraction().extRegxParam(response, YamlFile)
        if isinstance(Result,list):
            for i in Result:
                YamlParser(self.Yaml).setYaml(i, (Ptuple[Result.index(i)],))
