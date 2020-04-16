from requests_toolbelt import MultipartEncoder
from tools.Regular import *
from common.base import *
from common.Log import *
from tools.Rjson import *
from common.DataSource import *
from public.YamlParser import *
from public.BeParamCom import *


class TestCaseAssembly():

    def __init__(self):
        self.log = Log()
        self.Yaml = DataSource()

    def setAipParam(self, AipFile,Value,Dtuple:tuple,headers = None):
        '''接口参数组装'''
        intFile = YamlParser(AipFile)
        headers = self.Yaml.getHearder(headers)
        method = intFile.getYamlParms(('method',))
        urls = intFile.getYamlParms(('urls',))
        YamlParser(AipFile).setYaml(Value,Dtuple)
        data = intFile.getYamlParms(('data',))
        return method,headers,urls,data




        # res = YzApi().lapi(method=C.getYamlParms('method'), urls=C.getYamlParms('urls'), data=C.getYamlParms('data'),
        #                    headers=self.Yaml.getHearder())
'''
    def getBasedata(self, casefile):
        '':param casefile:文件名
        ''
        y = YamlParser('StudentInfo')
        S = YamlParser('sUnvs')
        P = YamlParser('sPfsnByOnScholarship')
        R = YamlParser(casefile)
        T = YamlParser('sTaNotStop')
        F = YamlParser('showFeeList')

        Q = YamlParser('getOpenTestAreaByCity')
        D = YamlParser('getOpenPfsnByTaId')

        ''判断是否是国开''
        if casefile == 'GrecruitAdd':
            ''读取基础信息''
            R.setYaml(str(y.getYamlParms(('GK', 'recruitType'))), 'recruitType')
            R.setYaml(str(y.getYamlParms(('GK','grade'))), ('data', 'grade'))
            R.setYaml(str(y.getYamlParms(('GK', 'level'))), ('data', 'pfsnLevel'))
            R.setYaml(str(y.getYamlParms(('GK', 'scholarships'))), ('data', 'scholarship'))

            ''获取院校sUnvs''
            S.setYaml(y.getYamlParms('GK''recruitType'), 'data''ext1')
            sUnvs = YzApi().lapi(method=S.getYamlParms('method'), urls=S.getYamlParms('urls'),
                                 data=S.getYamlParms('data'), headers=self.Yaml.getHearder())
            sid = regx(sUnvs.text, S.getYamlParms('regx'))
            unvsid = sid[random.randint(0, len(sid) - 1)]
            self.log.info('国开院校ID:' + unvsid)
            R.setYaml(str(unvsid), 'data''unvsId')

            ''获取考区''
            Q.setYaml(R.getYamlParms('city'), ('data', 'ext1'))
            Q.setYaml(y.getYamlParms(('GK', 'level')), ('data', 'ext2'))
            Q.setYaml(y.getYamlParms(('GK', 'grade')), ('data', 'ext3'))
            Area = YzApi().lapi(method=Q.getYamlParms('method'), urls=Q.getYamlParms('urls'),
                                data=Q.getYamlParms('data'), headers=self.Yaml.getHearder())
            CityArea = regx(Area.text, Q.getYamlParms('regx'))
            Area_s = CityArea[random.randint(0, len(CityArea) - 1)]
            self.log.info('国开考区ID:' + str(Area_s[1]) + str(Area_s[0]))
            R.setYaml(str(Area_s[0]), ('data', 'taId'))
            R.setYaml(str(Area_s[1]), ('data','taName'))

            ''获取专业''
            D.setYaml(str(Area_s[0]), ('data', 'ext1'))
            D.setYaml(str(y.getYamlParms(('GK', 'level'))), ('data', 'ext2'))
            D.setYaml(str(y.getYamlParms(('GK', 'grade'))), ('data', 'ext3'))
            Tid = YzApi().lapi(method=D.getYamlParms('method'), urls=D.getYamlParms('urls'),
                               data=D.getYamlParms('data'), headers=self.Yaml.getHearder())
            Pfsn = regx(Tid.text, D.getYamlParms('regx'))
            Pfsn_s = Pfsn[random.randint(0, len(Pfsn) - 1)]
            self.log.info('国开专业ID:' + str(Pfsn_s[1]) + str(Pfsn_s[0]))
            R.setYaml(str(Pfsn_s[0]), ('data', 'pfsnId'))
            R.setYaml(str(Pfsn_s[1]), ('data', 'pfsnName'))
            R.setYaml(str(Pfsn_s[2]), ('data', 'pfsnCode'))

            ''获取收费标准''
            F.setYaml(Pfsn_s[0], ('data', 'pfsnId'))
            F.setYaml(Area_s[0], ('data', 'taId'))
            F.setYaml(y.getYamlParms(('GK', 'scholarships')), ('data', 'scholarship'))
            F.setYaml(y.getYamlParms(('GK', 'recruitType')), ('data', 'recruitType'))
            Free = YzApi().lapi(method=F.getYamlParms('method'), urls=F.getYamlParms('urls'),
                                data=F.getYamlParms('data'), headers=self.Yaml.getHearder())
            feeList = regx(Free.text, F.getYamlParms('regx'))
            self.log.info('国开收费标准:' + str(feeList[0]))
            R.setYaml(str(feeList[0]), ('data', 'feeList'))

        if casefile == 'CrecruitAdd':
            S.setYaml(y.getYamlParms(('CJ', 'recruitType')), ('data', 'ext1'))
            P.setYaml(y.getYamlParms(('CJ', 'level')), ('data', 'ext1'))
            P.setYaml(y.getYamlParms(('CJ', 'grade')), ('data', 'ext2'))
            sUnvs = YzApi().lapi(method=S.getYamlParms('method'), urls=S.getYamlParms('urls'),
                                 data=S.getYamlParms('data'), headers=self.Yaml.getHearder())
            sid = regx(sUnvs.text, S.getYamlParms('regx'))
            unvsid = sid[random.randint(0, len(sid) - 1)]
            self.log.info('成教院校ID:' + unvsid)
            ''组装参数''
            P.setYaml(unvsid, ('data', 'sId'))
            R.setYaml(str(unvsid), ('data', 'unvsId'))
            R.setYaml(str(y.getYamlParms(('CJ', 'level'))), ('data', 'pfsnLevel'))
            R.setYaml(str(y.getYamlParms(('CJ', 'recruitType'))), ('data', 'recruitType'))
            F.setYaml(y.getYamlParms(('CJ', 'recruitType')), ('data', 'recruitType'))
            R.setYaml(str(y.getYamlParms(('CJ', 'grade'))), ('data', 'grade'))
            R.setYaml(str(y.getYamlParms(('CJ', 'scholarships'))), ('data', 'scholarship'))
            F.setYaml(y.getYamlParms(('CJ', 'scholarships')), ('data', 'scholarship'))

            ''获取专业''
            response = YzApi().lapi(method=P.getYamlParms('method'), urls=P.getYamlParms('urls'),
                                    data=P.getYamlParms('data'), headers=self.Yaml.getHearder())
            pid = regx(response.text, P.getYamlParms('regx'))
            pfsnid = pid[random.randint(0, len(pid) - 1)]
            self.log.info('成教专业ID:' + pfsnid)
            R.setYaml(str(pfsnid), ('data', 'pfsnId'))
            F.setYaml(pfsnid, ('data', 'pfsnId'))
            T.setYaml(pfsnid, ('data', 'sId'))

            ''获取考区''
            response1 = YzApi().lapi(method=T.getYamlParms('method'), urls=T.getYamlParms('urls'),
                                     data=T.getYamlParms('data'), headers=self.Yaml.getHearder())
            tid = regx(response1.text, T.getYamlParms('regx'))
            taId = tid[random.randint(0, len(tid) - 1)]
            self.log.info('成教考区ID:' + taId)
            R.setYaml(str(taId), ('data', 'taId'))
            F.setYaml(taId, ('data', 'taId'))
            ''获取收费标准''
            response2 = YzApi().lapi(method=F.getYamlParms('method'), urls=F.getYamlParms('urls'),
                                     data=F.getYamlParms('data'), headers=self.Yaml.getHearder())
            feeList = regx(response2.text, F.getYamlParms('regx'))
            self.log.info('成教收费标准:' + str(feeList[0]))
            R.setYaml(str(feeList[0]), ('data', 'feeList'))
            ''写回到yaml文件
'''
'''
    def getRegisterTestCaseData(self, casefile):
        '':获取学员注册所需data:param casefile:参数所在文件名:return:
        ''
        self.getBasedata(casefile)
        Yaml = YamlParser(casefile)
        HYaml = YamlParser('Hearder')
        Yaml.setYaml(YzApi().getBaseinfo('idCard'), ('data', 'idCard'))
        self.log.info(casefile + '身份证：' + Yaml.getYamlParms(('data', 'idCard')))
        Yaml.setYaml(YzApi().getBaseinfo('mobile'), ('data', 'mobile'))
        self.log.info(casefile + '手机号：' + Yaml.getYamlParms(('data', 'mobile')))
        data = MultipartEncoder(fields=Yaml.getYamlParms('data'))
        HYaml.setYaml(data.content_type, ('RHearders', 'Content-Type'))
        headers = HYaml.getYamlParms('RHearders')
        method = Yaml.getYamlParms('method')
        urls = Yaml.getYamlParms('urls')
        self.Yaml.setYaml(Yaml, casefile)
        return method, headers, urls, data

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