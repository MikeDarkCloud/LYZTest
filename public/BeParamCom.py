from common.base import YzApi
from common.conf import *
from common.DataSource import *
from public.YamlParser import *
class BeParamCom():

  def setAipData(self,AipFile,PaDict:dict):
    '''获取接口请求参数'''
    '''从模板,配置文件或提取参数中组合'''
    data0 = YamlParser(AipFile)
    for k in PaDict.keys():
        data0.setYaml(k,PaDict[k]) #(值：key)
    return YamlParser(AipFile).Yaml['data']


  def getPhone(self):
    return YzApi().getBaseinfo('mobile')

  def getCard(self):
    return YzApi().getBaseinfo('idCard')