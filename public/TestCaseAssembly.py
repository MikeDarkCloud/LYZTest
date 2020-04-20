from common.Log import *
from public.BeParamCom import *


class TestCaseAssembly():

    def __init__(self):
        self.log = Log()
        self.Yaml = DataSource()

    def setAipParam(self, AipFile,Value:tuple,Dtuple:tuple,headers = None):
        '''接口参数组装'''
        intFile = YamlParser(AipFile)
        headers = self.Yaml.getHearder(headers)
        method = intFile.getYamlParms(('method',))
        urls = intFile.getYamlParms(('urls',))
        i = 0
        while (i < len(Dtuple)):
            intFile.setYaml(Value[i:i+5], Dtuple[i:i+5])
            i = i + 5

        data = intFile.Yaml['data']
        return method,headers,urls,data

'''
    def getPayData(self):
        ''财务管理搜索结果获取learn_id''
        Hearder = YamlParser('Hearder')
        CYaml = YamlParser('CrecruitAdd')
        R = YamlParser('stdFeeList')
        R.setYaml(CYaml.getYamlParms(('data', 'mobile')), ('data', 'mobile'))
        response = YzApi().lapi(method=R.getYamlParms('method'), urls=R.getYamlParms('urls'),
                                data=R.getYamlParms('data'), headers=Hearder.getYamlParms('Hearders0'))
        ldict = getJsonParm(response.text, 'body')
        FYaml = YamlParser('toPay')
        FYaml.setYaml(str(ldict['data'][0]['learnId']), ('data', 'learnId'))
        self.Yaml.setLearnInfo('CStudent', 'learnId', str(ldict['data'][0]['learnId']))
        
        
        toPay = YzApi().lapi(method=FYaml.getYamlParms('method'), urls=FYaml.getYamlParms('urls'),
                             data=FYaml.getYamlParms('data'), headers=Hearder.getYamlParms('Hearders0'))
        Order = regx(toPay.text, FYaml.getYamlParms('regx0'))
        webtoken = regx(toPay.text, FYaml.getYamlParms('regx1'))
        PYaml = YamlParser('pay')
        Ldict = getJsonParm(Order[0], 'tutorPayInfos')[0]
        PYaml.setYaml(webtoken[0], ('data', '_web_token'))
        PYaml.setYaml(self.Yaml.getRallyaml('StudentInfo')['CJ']['grade'], ('data', 'grade'))
        PYaml.setYaml(Ldict['payable'], ('data', 'payableCount'))
        PYaml.setYaml(Ldict['payable'], ('data', 'payData', 'payAmount'))
        PYaml.setYaml(Ldict['payable'], ('data', 'payData', 'items', 0, 'amount'))
        PYaml.setYaml(self.Yaml.getLearnInfo('CStudent', 'learnId'), ('data', 'payData', 'learnId'))
        PYaml.setYaml(Ldict['payable'], ('data', 'payData', 'items', 0, 'payAmount'))
        PYaml.setYaml(self.Yaml.getLearnInfo('CStudent', 'learnId'), ('data', 'learnId'))
        PYaml.setYaml(Ldict['subOrderNo'], ('data', 'payData', 'items', 0, 'orderNo'))
        PPYaml = self.Yaml.getRallyaml('pay')
        items = PYaml.getYamlParms(('data', 'payData', 'items'))
        PPYaml['data']['payData']['items'] = str(items)
        PPYaml['data']['payData'] = str(getJson(PYaml['data']['payData']))
        data = PPYaml['data']
        method = PYaml.getYamlParms('method')
        headers = Hearder.getYamlParms('PHearder')
        urls = PYaml.getYamlParms('urls')
        return method, headers, urls, data
'''