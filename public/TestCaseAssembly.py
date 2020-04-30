'''
@description:api参数组装
@author:lanmingyong
'''
from common.Log import *
from public.BeforeParamCom import *


class TestCaseAssembly():

    def __init__(self):
        self.log = Log()
        self.Yaml = DataSource()

    def setAipParam(self, AipFile, Value:tuple, Keys:tuple, headers = None):
        '''接口参数组装'''
        intFile = YamlParser(AipFile)
        headers = self.Yaml.getHearder(headers)
        method = intFile.getYamlParms(('method',))
        urls = intFile.getYamlParms(('urls',))
        i = 0
        while (i < len(Keys)):
            V = Value[i:i + 5]
            if len(Value[i:i+5]) == 1 and isinstance(Value[i:i+5],tuple):
                V = Value[i:i + 5][0]
                intFile.setYaml(V, Keys[i:i + 5])
            else:
                intFile.setYaml(V, Keys[i:i + 5])
            i = i + 5
        # data = intFile.Yaml['data']
        data =intFile.getYamlParms(('data',))
        return method,headers,urls,data
