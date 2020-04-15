import random

from public.DataExtraction import *
class AfParamCom(DataExtraction):
    '''处理接口请求返回参数提取并保存'''
    def __init__(self):
        '''保存参数文件'''
        self.Yaml = 'LearnInfo'

    def saveParam(self,response,YamlFile,Ptuple:tuple):
        Result=DataExtraction().extRegxParam(response,YamlFile)
        #param是一个tuple
        param = Result[random.randint(0, len(Result) - 1)]
        if isinstance(param,tuple):
            for i in Ptuple:
                t = i
                p =param[Ptuple.index(i)]
                YamlParser(self.Yaml).setYaml(param[Ptuple.index(i)], (i,))
        else:
            YamlParser(self.Yaml).setYaml(param,(Ptuple,))

