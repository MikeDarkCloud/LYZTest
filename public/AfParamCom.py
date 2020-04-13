import random

from public.DataExtraction import *
class AfParamCom(DataExtraction):
    '''处理接口请求返回参数提取并保存'''
    def __init__(self):
        self.Yaml = 'LearnInfo'

    def saveParam(self,response,YamlFile,Ptuple):
        Result=DataExtraction().extRegxParam(response,YamlFile)
        #param是一个tuple
        param = Result[random.randint(0, len(Result) - 1)]
        if isinstance(param,(tuple)):
            for i in Ptuple:
                YamlParser(self.Yaml).setYaml(str(param[i]), Ptuple[i])
        YamlParser(self.Yaml).setYaml(str(param),Ptuple)

