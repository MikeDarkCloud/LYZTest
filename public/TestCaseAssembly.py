from requests_toolbelt import MultipartEncoder
from tools.Regular import *
from common.base import *
from common.Log import *
from tools.Rjson import *
from common.DataSource import *
from public.YamlParser import *

class TestCaseAssembly():

    def __init__(self):
        self.log = Log()
        self.Yaml = DataSource()

    def getBasedata(self,casefile):
        '''
        :param casefile:文件名
        '''
        H = self.Yaml.getRallyaml('Hearder')
        y = self.Yaml.getRallyaml('StudentInfo')
        S = self.Yaml.getRallyaml('sUnvs')
        P = self.Yaml.getRallyaml('sPfsnByOnScholarship')
        R = self.Yaml.getRallyaml(casefile)
        T = self.Yaml.getRallyaml('sTaNotStop')
        F = self.Yaml.getRallyaml('showFeeList')
        C = self.Yaml.getRallyaml('getGkOpenEnrollCityInfo')
        Q = self.Yaml.getRallyaml('getOpenTestAreaByCity')
        D = self.Yaml.getRallyaml('getOpenPfsnByTaId')

        '''判断是否是国开'''
        if casefile == 'GrecruitAdd':
            '''读取基础信息'''
            R['recruitType'] = str(y['GK']['recruitType'])
            R['data']['grade'] = str(y['GK']['grade'])
            R['data']['pfsnLevel'] = str(y['GK']['level'])
            R['data']['scholarship'] = str(y['GK']['scholarships'])
            '''获取城市getGkOpenEnrollCityInfo'''
            C['data']['ext1'] = y['GK']['level']
            C['data']['ext2'] = y['GK']['grade']
            res = YzApi().lapi(method=C.get('method'), urls=C.get('urls'), data=C.get('data'), headers=self.Yaml.getHearder())
            Code = regx(res.text, C.get('regx'))
            cityCode = Code[random.randint(0, len(Code) - 1)]
            self.log.info('国开城市ID:' + cityCode)
            R['data']['city'] = str(cityCode)
            '''获取院校sUnvs'''
            S['data']['ext1'] = y['GK']['recruitType']
            sUnvs = YzApi().lapi(method=S.get('method'), urls=S.get('urls'), data=S.get('data'), headers=self.Yaml.getHearder())
            sid = regx(sUnvs.text, S.get('regx'))
            unvsid = sid[random.randint(0, len(sid) - 1)]
            self.log.info('国开院校ID:' + unvsid)
            R['data']['unvsId'] = str(unvsid)

            '''获取考区'''
            Q['data']['ext1'] = str(cityCode)
            Q['data']['ext2'] = y['GK']['level']
            Q['data']['ext3'] = y['GK']['grade']
            Area = YzApi().lapi(method=Q.get('method'), urls=Q.get('urls'), data=Q.get('data'), headers=self.Yaml.getHearder())
            CityArea = regx(Area.text, Q.get('regx'))
            Area_s = CityArea[random.randint(0, len(CityArea) - 1)]
            self.log.info('国开考区ID:' + str(Area_s[1])+str(Area_s[0]))
            R['data']['taId'] = str(Area_s[0])
            R['data']['taName'] = str(Area_s[1])
            '''获取专业'''
            D['data']['ext1'] = str(Area_s[0])
            D['data']['ext2'] = str(y['GK']['level'])
            D['data']['ext3'] = str(y['GK']['grade'])
            Tid = YzApi().lapi(method=D.get('method'), urls=D.get('urls'), data=D.get('data'), headers=self.Yaml.getHearder())
            Pfsn = regx(Tid.text, D.get('regx'))
            Pfsn_s = Pfsn[random.randint(0, len(Pfsn) - 1)]
            self.log.info('国开专业ID:' + str(Pfsn_s[1])+str(Pfsn_s[0]))
            R['data']['pfsnId'] = str(Pfsn_s[0])
            R['data']['pfsnName'] = str(Pfsn_s[1])
            R['data']['pfsnCode'] = str(Pfsn_s[2])

            '''获取收费标准'''
            F['data']['pfsnId'] = Pfsn_s[0]
            F['data']['taId'] = Area_s[0]
            F['data']['scholarship'] = y['GK']['scholarships']
            F['data']['recruitType'] = y['GK']['recruitType']
            Free = YzApi().lapi(method=F.get('method'), urls=F.get('urls'), data=F.get('data'), headers=self.Yaml.getHearder())
            feeList = regx(Free.text, F.get('regx'))
            self.log.info('国开收费标准:' + str(feeList[0]))
            R['data']['feeList'] = str(feeList[0])

            self.Yaml.setYaml(R, casefile)

        if casefile == 'CrecruitAdd':
            S['data']['ext1'] = y['CJ']['recruitType']
            P['data']['ext1']=y['CJ']['level']
            P['data']['ext2']=y['CJ']['grade']
            sUnvs = YzApi().lapi(method = S.get('method'),urls =S.get('urls'),data =S.get('data'),headers =self.Yaml.getHearder())
            sid = regx(sUnvs.text, S.get('regx'))
            unvsid=sid[random.randint(0, len(sid)-1)]
            self.log.info('成教院校ID:' + unvsid)
            '''组装参数'''
            P['data']['sId']= unvsid
            R['data']['unvsId'] = str(unvsid)
            R['data']['pfsnLevel'] = str(y['CJ']['level'])
            R['data']['recruitType'] = str(y['CJ']['recruitType'])
            F['data']['recruitType'] = y['CJ']['recruitType']
            R['data']['grade'] = str(y['CJ']['grade'])
            R['data']['scholarship'] = str(y['CJ']['scholarships'])
            F['data']['scholarship'] = y['CJ']['scholarships']

            '''获取专业'''
            response = YzApi().lapi(method = P.get('method'),urls =P.get('urls'),data =P.get('data'),headers =self.Yaml.getHearder())
            pid = regx(response.text, P.get('regx'))
            pfsnid = pid[random.randint(0, len(pid)-1)]
            self.log.info('成教专业ID:' + pfsnid)
            R['data']['pfsnId'] =str(pfsnid)
            F['data']['pfsnId'] =pfsnid
            T['data']['sId'] = pfsnid

            '''获取考区'''
            response1 = YzApi().lapi(method=T.get('method'), urls=T.get('urls'), data=T.get('data'), headers=self.Yaml.getHearder())
            tid = regx(response1.text, T.get('regx'))
            taId = tid[random.randint(0, len(tid)-1)]
            self.log.info('成教考区ID:' + taId)
            R['data']['taId'] = str(taId)
            F['data']['taId'] = taId
            '''获取收费标准'''
            response2 = YzApi().lapi(method=F.get('method'), urls=F.get('urls'), data=F.get('data'), headers=self.Yaml.getHearder())
            feeList = regx(response2.text, F.get('regx'))
            self.log.info('成教收费标准:' + str(feeList[0]))
            R['data']['feeList'] = str(feeList[0])
            '''写回到yaml文件'''
            self.Yaml.setYaml(R,casefile)

    def getRegisterTestCaseData(self,casefile):
        '''
        :获取学员注册所需data
        :param casefile:参数所在文件名
        :return: tuple
        '''
        self.getBasedata(casefile)
        Yaml = self.Yaml.getRallyaml(casefile)
        HYaml = self.Yaml.getRallyaml('Hearder')
        Yaml['data']['idCard'] = YzApi().getBaseinfo('idCard')
        self.log.info(casefile+'身份证：'+Yaml['data']['idCard'])
        Yaml['data']['mobile'] = YzApi().getBaseinfo('mobile')
        self.log.info(casefile+'手机号：' + Yaml['data']['mobile'])
        data = MultipartEncoder(fields=Yaml['data'])
        HYaml['RHearders']['Content-Type'] = data.content_type
        headers = HYaml['RHearders']
        method = Yaml['method']
        urls = Yaml['urls']
        self.Yaml.setYaml(Yaml,casefile)
        return method,headers,urls,data


    def getPayData(self):
        '''财务管理搜索结果获取learn_id'''
        Hearder = YamlParser('Hearder')
        CYaml = YamlParser('CrecruitAdd')
        R=YamlParser('stdFeeList')
        R.setYaml(CYaml.getYamlParms('data','mobile'),'data','mobile')
        self.Yaml.setYaml(R, 'stdFeeList')
        response = YzApi().lapi(method=R.getYamlParms('method'), urls=R.getYamlParms('urls'), data=R.getYamlParms('data'), headers=Hearder.getYamlParms('Hearders0'))
        ldict = getJsonParm(response.text,'body')
        FYaml = YamlParser('toPay')
        FYaml.setYaml(str(ldict['data'][0]['learnId']),'data','learnId')
        self.Yaml.setYaml(FYaml,'toPay')
        self.Yaml.setLearnInfo('CStudent','learnId',str(ldict['data'][0]['learnId']))
        toPay = YzApi().lapi(method=FYaml.getYamlParms('method'), urls=FYaml.getYamlParms('urls'), data=FYaml.getYamlParms('data'), headers=Hearder.getYamlParms('Hearders0'))
        Order = regx(toPay.text, FYaml.getYamlParms('regx0'))
        webtoken = regx(toPay.text, FYaml.getYamlParms('regx1'))
        PYaml = YamlParser('pay')
        Ldict = getJsonParm(Order[0],'tutorPayInfos')[0]
        PYaml.setYaml(webtoken[0],'data','_web_token')
        PYaml.setYaml(self.Yaml.getRallyaml('StudentInfo')['CJ']['grade'],'data','grade')
        PYaml['data']['payableCount'] = Ldict['payable']
        PYaml['data']['payData']['payAmount']=Ldict['payable']
        PYaml['data']['payData']['items'][0]['amount']=Ldict['payable']
        PYaml['data']['payData']['learnId'] = self.Yaml.getLearnInfo('CStudent','learnId')
        PYaml['data']['payData']['items'][0]['payAmount']=Ldict['payable']
        PYaml['data']['learnId'] = self.Yaml.getLearnInfo('CStudent','learnId')
        PYaml['data']['payData']['items'][0]['orderNo']=Ldict['subOrderNo']
        self.Yaml.setYaml(PYaml,'pay')
        PPYaml = self.Yaml.getRallyaml('pay')
        items =PYaml['data']['payData']['items']
        PPYaml['data']['payData']['items'] = str(items)
        PPYaml['data']['payData'] = str(getJson(PYaml['data']['payData']))
        data = PPYaml['data']
        method = PYaml['method']
        headers = Hearder.getYamlParms('PHearder')
        urls = PYaml['urls']
        return method, headers, urls, data



