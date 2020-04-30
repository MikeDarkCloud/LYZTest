from common.base import YzApi
from public.YamlParser import *


class BeforeParamCom():

    def setAipData(self, AipFile, keys: dict):
        '''获取接口请求参数'''
        '''从模板,配置文件或提取参数中组合'''
        data0 = YamlParser(AipFile)
        for k in keys.keys():
            data0.setYaml(k, keys[k])
        return YamlParser(AipFile).Yaml['data']

    def getPhone(self):
        return YzApi().getBaseinfo('mobile')

    def getCard(self):
        return YzApi().getBaseinfo('idCard')

    def setLearn(self, key: tuple, value):
        '''保存信息到LearnInfo文件'''
        YamlParser('LearnInfo').setYaml(value, key)
