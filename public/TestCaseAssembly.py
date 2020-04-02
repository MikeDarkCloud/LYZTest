from requests_toolbelt import MultipartEncoder
from tools.Regular import *
from common.base import *
import  random
from common.Log import *
class TestCaseAssembly():

    def __init__(self):
        # self.y = Config().Rallyaml('regiester')
        self.log = Log()

    '''获取接口返回数据'''
    def getBasedata(self,r,casefile):
        '''
        :param r:请求实例
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
        if casefile == 'Gkregiester':
            '''读取基础信息'''
            R['recruitType'] = str(y['GK']['recruitType'])
            R['data']['grade'] = str(y['GK']['grade'])
            R['data']['pfsnLevel'] = str(y['GK']['level'])
            R['data']['scholarship'] = str(y['GK']['scholarships'])
            '''获取城市getGkOpenEnrollCityInfo'''
            C['data']['ext1'] = y['GK']['level']
            C['data']['ext2'] = y['GK']['grade']
            res = r.lapi(method=C['method'], urls=C['urls'], data=C['data'], headers=H['hearders0'])
            Code = regx(res.text, C['regx'])
            cityCode = Code[random.randint(0, len(Code) - 1)]
            R['data']['city'] = str(cityCode)
            '''获取院校sUnvs'''
            S['data']['ext1'] = y['GK']['recruitType']
            sUnvs = r.lapi(method=S['method'], urls=S['urls'], data=S['data'], headers=H['hearders0'])
            sid = regx(sUnvs.text, S['regx'])
            unvsid = sid[random.randint(0, len(sid) - 1)]
            R['data']['unvsId'] = str(unvsid)

            '''获取考区'''
            Q['data']['ext1'] = str(cityCode)
            Q['data']['ext2'] = y['GK']['level']
            Q['data']['ext3'] = y['GK']['grade']
            Area = r.lapi(method=Q['method'], urls=Q['urls'], data=Q['data'], headers=H['hearders0'])
            CityArea = regx(Area.text, Q['regx'])
            Area_s = CityArea[random.randint(0, len(CityArea) - 1)]
            R['data']['taId'] = str(Area_s[0])
            R['data']['taName'] = str(Area_s[1])
            '''获取专业'''
            D['data']['ext1'] = str(Area_s[0])
            D['data']['ext2'] = str(y['GK']['level'])
            D['data']['ext3'] = str(y['GK']['grade'])
            Tid = r.lapi(method=D['method'], urls=D['urls'], data=D['data'], headers=H['hearders0'])
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
            Free = r.lapi(method=F['method'], urls=F['urls'], data=F['data'], headers=H['hearders0'])
            feeList = regx(Free.text, F['regx'])
            R['data']['feeList'] = str(feeList[0])

            Config().Wyaml(R, casefile)

        if casefile == 'regiester':
            S['data']['ext1'] = y['CJ']['recruitType']
            P['data']['ext1']=y['CJ']['level']
            P['data']['ext2']=y['CJ']['grade']
            sUnvs = r.lapi(method = S['method'],urls =S['urls'],data =S['data'],headers =H['hearders0'])
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
            response = r.lapi(method = P['method'],urls =P['urls'],data =P['data'],headers =H['hearders0'])
            pid = regx(response.text, P['regx'])
            pfsnid = pid[random.randint(0, len(pid)-1)]
            R['data']['pfsnId'] =str(pfsnid)
            F['data']['pfsnId'] =pfsnid
            T['data']['sId'] = pfsnid

            '''获取考区'''
            response1 = r.lapi(method=T['method'], urls=T['urls'], data=T['data'], headers=H['hearders0'])
            tid = regx(response1.text, T['regx'])
            taId = tid[random.randint(0, len(tid)-1)]
            R['data']['taId'] = str(taId)
            F['data']['taId'] = taId
            '''获取收费标准'''
            response2 = r.lapi(method=F['method'], urls=F['urls'], data=F['data'], headers=H['hearders0'])
            feeList = regx(response2.text, F['regx'])
            R['data']['feeList'] = str(feeList[0])
            '''写回到yaml文件'''
            Config().Wyaml(R,casefile)

    def getRegisterTestCaseData(self,r,casefile):
        '''
        :param r:请求实例
        :param casefile:参数所在文件名
        :return: tuple
        '''
        self.getBasedata(r,casefile)
        y = Config().Rallyaml(casefile)
        y['data']['idCard'] = r.getBaseinfo('idCard')
        y['data']['mobile'] = r.getBaseinfo('mobile')
        data = MultipartEncoder(fields=y['data'])
        y['hearders']['Content-Type'] = data.content_type
        headers = y['hearders']
        method = y['method']
        urls = y['urls']
        Config().Wyaml(y,casefile)
        return method,headers,urls,data






