import random
from public.DataExtraction import *
from tools.Rjson import *
class AfterParamCom(DataExtraction):
    '''处理接口请求返回参数提取并保存'''
    def __init__(self):
        '''保存参数文件'''
        self.Yaml = 'LearnInfo'

    def saveParam(self, response, YamlFile, Keys:tuple):
        '''正则提取参数并保存'''
        Result=DataExtraction().extRegxParam(response,YamlFile)
        param = Result[random.randint(0, len(Result) - 1)]
        if isinstance(param,tuple):
            for i in Keys:
                YamlParser(self.Yaml).setYaml(param[Keys.index(i)], (i,))
        else:
            YamlParser(self.Yaml).setYaml(param, (Keys,))


    def saveJson(self,response,key0:tuple,key1:tuple):
        '''转为josn方式提取参数并保存'''
        jsonp = getJsonParm(response)
        for i in key0:
            value = readDict(jsonp,i)
            YamlParser(self.Yaml).setYaml(str(value), (key1[key0.index(i)],))


    def moreParam(self, response, YamlFile, keys:tuple):
        '''多个正则表达式提取参数并保存'''
        Result = DataExtraction().extRegxParam(response, YamlFile)
        if isinstance(Result,list):
            for i in Result:
                YamlParser(self.Yaml).setYaml(str(i), (keys[Result.index(i)],))

