from requests_toolbelt import MultipartEncoder
from tools.Regular import *
from common.base import *
from common.Log import *
from tools.Rjson import *
class TestCaseAssembly():

    def __init__(self):
        # self.y = Config().Rallyaml('CrecruitAdd')
        self.log = Log()

    '''获取接口返回数据'''
    def getBasedata(self,casefile):
        '''
        :param casefile:文件名
        '''
        H = Config().Rallyaml('Hearder')
        y = Config().Rallyaml('StudentInfo')
        S = Config().Rallyaml('sUnvs')
        P = Config().Rallyaml('sPfsnByOnScholarship')
        R = Config().Rallyaml(casefile)
        T = Config().Rallyaml('sTaNotStop')
        F = Config().Rallyaml('showFeeList')
        C = Config().Rallyaml('getGkOpenEnrollCityInfo')
        Q = Config().Rallyaml('getOpenTestAreaByCity')
        D = Config().Rallyaml('getOpenPfsnByTaId')

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
            res = YzApi().lapi(method=C['method'], urls=C['urls'], data=C['data'], headers=H['Hearders0'])
            Code = regx(res.text, C['regx'])
            cityCode = Code[random.randint(0, len(Code) - 1)]
            R['data']['city'] = str(cityCode)
            '''获取院校sUnvs'''
            S['data']['ext1'] = y['GK']['recruitType']
            sUnvs = YzApi().lapi(method=S['method'], urls=S['urls'], data=S['data'], headers=H['Hearders0'])
            sid = regx(sUnvs.text, S['regx'])
            unvsid = sid[random.randint(0, len(sid) - 1)]
            R['data']['unvsId'] = str(unvsid)

            '''获取考区'''
            Q['data']['ext1'] = str(cityCode)
            Q['data']['ext2'] = y['GK']['level']
            Q['data']['ext3'] = y['GK']['grade']
            Area = YzApi().lapi(method=Q['method'], urls=Q['urls'], data=Q['data'], headers=H['Hearders0'])
            CityArea = regx(Area.text, Q['regx'])
            Area_s = CityArea[random.randint(0, len(CityArea) - 1)]
            R['data']['taId'] = str(Area_s[0])
            R['data']['taName'] = str(Area_s[1])
            '''获取专业'''
            D['data']['ext1'] = str(Area_s[0])
            D['data']['ext2'] = str(y['GK']['level'])
            D['data']['ext3'] = str(y['GK']['grade'])
            Tid = YzApi().lapi(method=D['method'], urls=D['urls'], data=D['data'], headers=H['Hearders0'])
            Pfsn = regx(Tid.text, D['regx'])
            Pfsn_s = Pfsn[random.randint(0, len(Pfsn) - 1)]
            R['data']['pfsnId'] = str(Pfsn_s[0])
            R['data']['pfsnName'] = str(Pfsn_s[1])
            R['data']['pfsnCode'] = str(Pfsn_s[2])

            '''获取收费标准'''
            F['data']['pfsnId'] = Pfsn_s[0]
            F['data']['taId'] = Area_s[0]
            F['data']['scholarship'] = y['GK']['scholarships']
            F['data']['recruitType'] = y['GK']['recruitType']
            Free = YzApi().lapi(method=F['method'], urls=F['urls'], data=F['data'], headers=H['Hearders0'])
            feeList = regx(Free.text, F['regx'])
            R['data']['feeList'] = str(feeList[0])

            Config().Wyaml(R, casefile)

        if casefile == 'CrecruitAdd':
            S['data']['ext1'] = y['CJ']['recruitType']
            P['data']['ext1']=y['CJ']['level']
            P['data']['ext2']=y['CJ']['grade']
            sUnvs = YzApi().lapi(method = S['method'],urls =S['urls'],data =S['data'],headers =H['Hearders0'])
            sid = regx(sUnvs.text, S['regx'])
            unvsid=sid[random.randint(0, len(sid)-1)]
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
            response = YzApi().lapi(method = P['method'],urls =P['urls'],data =P['data'],headers =H['Hearders0'])
            pid = regx(response.text, P['regx'])
            pfsnid = pid[random.randint(0, len(pid)-1)]
            R['data']['pfsnId'] =str(pfsnid)
            F['data']['pfsnId'] =pfsnid
            T['data']['sId'] = pfsnid

            '''获取考区'''
            response1 = YzApi().lapi(method=T['method'], urls=T['urls'], data=T['data'], headers=H['Hearders0'])
            tid = regx(response1.text, T['regx'])
            taId = tid[random.randint(0, len(tid)-1)]
            R['data']['taId'] = str(taId)
            F['data']['taId'] = taId
            '''获取收费标准'''
            response2 = YzApi().lapi(method=F['method'], urls=F['urls'], data=F['data'], headers=H['Hearders0'])
            feeList = regx(response2.text, F['regx'])
            R['data']['feeList'] = str(feeList[0])
            '''写回到yaml文件'''
            Config().Wyaml(R,casefile)

    def getRegisterTestCaseData(self,casefile):
        '''
        :param casefile:参数所在文件名
        :return: tuple
        '''
        self.getBasedata(casefile)
        y = Config().Rallyaml(casefile)
        y['data']['idCard'] = YzApi().getBaseinfo('idCard')
        self.log.info(casefile+'手机号：'+y['data']['idCard'])
        y['data']['mobile'] = YzApi().getBaseinfo('mobile')
        self.log.info(casefile+'身份证：' + y['data']['mobile'])
        data = MultipartEncoder(fields=y['data'])
        y['hearders']['Content-Type'] = data.content_type
        headers = y['hearders']
        method = y['method']
        urls = y['urls']
        Config().Wyaml(y,casefile)
        return method,headers,urls,data


    def getStdFeeList(self):
        '''财务管理搜索结果获取learn_id'''
        H = Config().Rallyaml('Hearder')
        R=Config().Rallyaml('stdFeeList')['data']['mobile'] = Config().Rallyaml('CrecruitAdd')['data']['mobile']
        Config().Wyaml(R, 'stdFeeList')
        response = YzApi().lapi(method=R['method'], urls=R['urls'], data=R['data'], headers=H['Hearders0'])
        learn_id = regx(response.text, R['regx'])
        return learn_id[0]


    def getPayData(self):
        H = Config().Rallyaml('Hearder')
        R = Config().Rallyaml('toPay')['learnId'] = self.getStdFeeList()
        Config().Wyaml(R, 'toPay')
        response = YzApi().lapi(method=R['method'], urls=R['urls'], data=R['data'], headers=H['Hearders0'])
        response_text = regx(response.text, R['regx'])
        response_text = regx(response.text, R['regx'])
        value = getJsonParm(response_text[0],'payInfos')
        P = Config().Rallyaml('pay')
        P['data']['payData']['items'][0]['orderNo'] = value[0]['subOrderNo']


