from common.conf import *
from common.DataSource import *
from public.YamlParser import *
class BeParamCom():

  def setAipData(self,AipFile,PaDict:dict):
    '''获取接口请求参数'''
    '''从模板,配置文件或提取参数中组合'''
    data0 = YamlParser(AipFile)
    for k in PaDict.keys():
        g= k
        t= PaDict[k]
        data0.setYaml(k,PaDict[k]) #(值：key)
    return YamlParser(AipFile).Yaml['data']


