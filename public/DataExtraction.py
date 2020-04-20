from public.YamlParser import *
from tools.Regular import *
from tools.Rjson import *
class DataExtraction():
    '''
    :接口返回数据提取
    '''

    def extRegxParam(self,response,YamlFile):
        '''接口返回数据正则提取'''
        '''
        :response 请求响应
        :YamlFile 接口文件
        :return tuple 
        '''
        re =YamlParser(YamlFile).getYamlParms(('regx',))
        TX = []
        if isinstance(re,list):
            for i in re:
                TX.append(regx(response, i))
            return TX
        else:
            return regx(response, re)


    def extJsonParam(self,response,YamlFile):
        '''接口返回数据转Json提取'''
        pass
