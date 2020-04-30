'''
@description:接口响应参数提取
@author:lanmingyong
'''
from public.YamlParser import *
from tools.Regular import *

class DataExtraction():
    '''接口返回提取数据'''

    def extRegxParam(self,response,YamlFile):
        '''接口返回数据正则提取'''
        '''支持多个正则表达式'''
        re =YamlParser(YamlFile).getYamlParms(('regx',))
        TX = []
        if isinstance(re,list):
            for i in re:
                TX.append(regx(response, i)[0])
            return TX
        else:
            return regx(response, re)