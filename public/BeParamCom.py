from common.conf import *
from common.DataSource import *
from public.YamlParser import *
class BeParamCom():

  def getAipData(self,AipFile,PaDict:dict):
    '''获取接口请求参数'''
    '''从模板,配置文件或提取参数中组合'''
    data = YamlParser(AipFile)
    for k in PaDict.keys():
        data.setYaml(k,PaDict[k])

    return data


