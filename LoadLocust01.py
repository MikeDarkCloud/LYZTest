"""
@author:lanmingyong
@time:20200429
"""
from locust.clients import HttpSession
from locust import *
from common.DataSource import DataSource
from common.base import YzApi
from public.TestCaseAssembly import TestCaseAssembly, BeforeParamCom
from public.AfterParamCom import *
from requests_toolbelt import MultipartEncoder
import queue

class LoadLocust(TaskSet):
    def on_start(self):
        self.session = HttpSession('http://bms-3.yzwill.cn')

    @seq_task(1)
    def test_00_login(self):
        t= DataSource().getAllyaml('Logining')
        url = str(t.get('urls'))
        data = dict(t.get('data'))
        try:
            data['mobile']=self.locust.queueData.get()
            print(data)
        except queue.Empty:
            print('no data exit')
            exit(0)
        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        response = self.session.post(url=url,data=data, headers=headers,verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")

    def test_0_getGkOpenEnrollCityInfo(self):
        '''随机获取国开报读城市'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('getGkOpenEnrollCityInfo', (intFile.getYamlParms(('GK', 'grade'),), intFile.getYamlParms(('GK', 'level'))),
                                              (('data', 'ext2'), ('data', 'ext1')))

        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }

        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getGkOpenEnrollCityInfo', ('GStudent', 'city'))


    def test_1_sUnvs(self):
        '''随机获取国开院校ID'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('sUnvs', (intFile.getYamlParms(('GK', 'recruitType')),), ('data', 'ext1'))

        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'sUnvs', ('GStudent', 'unvsId'))


    def test_2_getOpenTestAreaByCity(self):
        '''随机获取国开报读考区ID+考区名称'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenTestAreaByCity', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'city'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))

        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getOpenTestAreaByCity', (('GStudent', 'taId'), ('GStudent', 'taName')))

    def test_3_getOpenPfsnByTaId(self):
        '''随机获取国开报读专业pfsnId+专业名称pfsnName+专业编号pfsnCode'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenPfsnByTaId', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'taId'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))
        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getOpenPfsnByTaId', (('GStudent', 'pfsnId'), ('GStudent', 'pfsnName'), ('GStudent', 'pfsnCode')))

    def test_4_showFeeList(self):
        '''获取国开报读收费标准信息'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('showFeeList', (
        intFile.getYamlParms(('GK', 'recruitType')), intFile.getYamlParms(('GK', 'scholarships')), extFile.getYamlParms(('GStudent', 'pfsnId')),
        extFile.getYamlParms(('GStudent', 'taId'))), (('data', 'recruitType'), ('data', 'scholarship'), ('data', 'pfsnId'), ('data', 'taId')))

        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        '''提取参数'''
        AfterParamCom().saveJson(response.text, (('body', 'feeInfo', 'feeId'),), (('GStudent', 'feeId'),))
        AfterParamCom().saveParam(response.text, 'showFeeList', ('GStudent', 'feeList'))


    def test_5_gk_normal_register(self):
        '''随机录入国开类型学员学员'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        '''从配置文件获取参数'''
        grade = intFile.getYamlParms(('GK', 'grade'))
        recruitType = intFile.getYamlParms(('GK', 'recruitType'))
        scholarship = intFile.getYamlParms(('GK', 'scholarships'))
        '''从参数文件获取参数'''
        city = extFile.getYamlParms(('GStudent', 'city'))
        unvsId = extFile.getYamlParms(('GStudent', 'unvsId'))
        feeId = extFile.getYamlParms(('GStudent', 'feeId'))
        feeList = extFile.getYamlParms(('GStudent', 'feeList'))
        pfsnCode = extFile.getYamlParms(('GStudent', 'pfsnCode'))
        pfsnId = extFile.getYamlParms(('GStudent', 'pfsnId'))
        pfsnName = extFile.getYamlParms(('GStudent', 'pfsnName'))
        taId = extFile.getYamlParms(('GStudent', 'taId'))
        taName = extFile.getYamlParms(('GStudent', 'taName'))
        mobile =BeforeParamCom().getPhone()
        idCard =BeforeParamCom().getCard()
        BeforeParamCom().setLearn((('GStudent', 'mobile'),), mobile)
        BeforeParamCom().setLearn((('GStudent', 'idCard'),), idCard)

        pfsnLevel = intFile.getYamlParms(('GK', 'pfsnLevel'))

        '''将参数组合到接口文件'''
        values = (str(grade),str(recruitType),str(scholarship),str(city),str(unvsId),str(feeList),str(pfsnCode),
                  str(pfsnId),str(pfsnName),str(taId),str(taName),mobile,idCard,str(pfsnLevel),str(feeId))
        keys = (('data', 'grade'),('data', 'recruitType'),('data', 'scholarship'),('data', 'city'),('data', 'unvsId'),
                ('data', 'feeList'), ('data', 'pfsnCode'), ('data', 'pfsnId'), ('data', 'pfsnName'), ('data', 'taId'),
                ('data', 'taName'),('data', 'mobile'),('data', 'idCard'),('data', 'pfsnLevel'),('data', 'feeId'))
        case = TestCaseAssembly().setAipParam('GrecruitAdd',values,keys,'regiester')
        data = MultipartEncoder(fields=case[3])

        headers = {
                  "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
                  "Host": 'bms-3.yzwill.cn',
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
                  }
        headers["Content-Type"] = data.content_type

        response = self.session.post(url=case[2], data=case[3], headers=headers, verify=False)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")

    @seq_task(2)
    def test_01_gkregister(self):
        self.test_0_getGkOpenEnrollCityInfo()
        self.test_1_sUnvs()
        self.test_2_getOpenTestAreaByCity()
        self.test_3_getOpenPfsnByTaId()
        self.test_4_showFeeList()
        self.test_5_gk_normal_register()

class WebsiteUser(HttpLocust):
    mobilList = [13510021464,13829984462,15220600630,13380931310,13928313848,18927311598,13302659358,
                 13516679719,13829946638,13825452808,13809837072,13302659300,13302659055,13249136327,
                 18824867989,13316363619,18927311599,13531712554,13422929660,18927311533,13302657779,
                 18927311595,18927311592,13428067693,15089561462,18316420155,13302659700,18927311515,
                 13809832588,18927319798,18927319792,13669506061,13630091278,13553278196,13202796139,
                 15976116484,13825418802,18688343794,15811902125,13421615643,13192809766,18689481992,
                 13928332330,13433532344,13680825687,15767368908,15118920995,18814449910,15767958977,
                 13794500533,15622720742,13728051069,18003017330,15766564346,18613095131,18825078109,
                 13631907254,15014449123,18200813197,13411221798,18129596682,15766295545,18825172583,
                 18820044450,13232693023,15622564436,17875050321,18219042689,13539022703,18923659367,
                 15016482831,13422955477,15516902516,18927383931,13719602899,13480506480,13794813633,
                 13437662001,14778580943,15815434130,15918654019,13428058683,13226629215,13318610486,
                 13750226525,15915842165,15277274655,13416620223,15916400624,13437732624,13531687922,
                 18923608195,15917771003,15159268034,15875253254,15976108610,13825059586,15817013917]
    task_set = LoadLocust
    host = "http://bms-3.yzwill.cn"
    queueData = queue.Queue()
    for i in mobilList:
        queueData.put(i)
    min_wait = 1000
    max_wait = 5000



