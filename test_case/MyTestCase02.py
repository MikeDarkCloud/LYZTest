from common.myunit import *
from ddt import ddt, data, unpack
from public.TestCaseAssembly import TestCaseAssembly, BeParamCom
from public.TestCaseAssert import MyAssert
from public.YamlParser import *
from public.AfParamCom import *
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor


class MyTestCase(StartEnd):

    def setUp(self):
        pass

    # @unittest.skip("skipping")
    def test_0_sUnvs(self):
        '''随机获取成教院校ID'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('sUnvs', (intFile.getYamlParms(('CJ', 'recruitType')),), ('data', 'ext1'))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'sUnvs', ('CStudent', 'unvsId'))

    # @unittest.skip("skipping")
    def test_1_sPfsnByOnScholarship(self):
        '''随机获取成教专业'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        grade = intFile.getYamlParms(('CJ', 'grade'))
        level = intFile.getYamlParms(('CJ', 'level'))
        sId = extFile.getYamlParms(('CStudent', 'unvsId'))
        values = (grade,level,sId)
        keys = (('data', 'ext2'),('data', 'ext1'),('data', 'sId'))
        case = TestCaseAssembly().setAipParam('sPfsnByOnScholarship',values,keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'sPfsnByOnScholarship', ('CStudent', 'pfsnId'))

    # @unittest.skip("skipping")
    def test_2_getOpenTestAreaByCity(self):
        '''随机获取考区'''
        extFile = YamlParser('LearnInfo')
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        values = (pfsnId,)
        keys = (('data', 'sId'),)
        case = TestCaseAssembly().setAipParam('sTaNotStop',values,keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'sTaNotStop', ('CStudent', 'taId'))

    # @unittest.skip("skipping")
    def test_3_showFeeList(self):
        '''获取收费标准'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        taId = extFile.getYamlParms(('CStudent', 'taId'))
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        scholarship = intFile.getYamlParms(('CJ', 'scholarships'))
        values = (pfsnId,taId,recruitType,scholarship)
        keys = (('data', 'pfsnId'),('data', 'taId'),('data', 'recruitType'),('data', 'scholarship'))
        case = TestCaseAssembly().setAipParam('showFeeList',values,keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'showFeeList', ('CStudent', 'feeList'))

    def test_4_CrecruitAdd(self):
        '''随机注册成教学员'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        '''提取到的'''
        unvsid = extFile.getYamlParms(('CStudent', 'unvsId'))
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        taId = extFile.getYamlParms(('CStudent', 'taId'))
        feeList = extFile.getYamlParms(('CStudent', 'feeList'))
        '''配置的'''
        scholarship = intFile.getYamlParms(('CJ', 'scholarships'))
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        grade = intFile.getYamlParms(('CJ', 'grade'))
        pfsnLevel = intFile.getYamlParms(('CJ', 'level'))
        mobile = BeParamCom().getPhone()
        idCard = BeParamCom().getCard()
        BeParamCom().setLearn((('CJ','mobile'),),mobile)
        BeParamCom().setLearn((('CJ','idCard'),),idCard)
        values = (str(unvsid),str(pfsnId),str(taId),str(feeList),str(scholarship),str(recruitType),str(grade),str(pfsnLevel),str(mobile),str(idCard))
        keys = (('data', 'unvsId'),('data', 'pfsnid'),('data', 'taId'),('data', 'feeList'),('data', 'scholarship')
                , ('data', 'recruitType'),('data', 'grade'),('data', 'pfsnLevel'),('data', 'mobile'),('data', 'idCard'))
        case = TestCaseAssembly().setAipParam('CrecruitAdd',values,keys)
        data = MultipartEncoder(fields=case[3])
        DataSource().setHearder(data.content_type)
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("regiester"), urls=case[2], data=data)
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_5_stdFeeList(self):
        '''财务管理搜索结果获取learn_id'''
        extFile = YamlParser('LearnInfo')
        mobile = extFile.getYamlParms(('CJ','mobile'))
        values = (mobile,)
        keys = (('data', 'mobile'),)
        case = TestCaseAssembly().setAipParam('stdFeeList',values,keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数learnId'''
        resJosn = getJsonParm(response.text, 'body')
        learnId = str(resJosn['data'][0]['learnId']), ('data', 'learnId')
        BeParamCom().setLearn((('CJ', 'learnId'),), learnId)


    @unittest.skip("skipping")
    def test_6_toPay(self):
        '''获取支付订单及web_token'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CJ','learnId'))
        values = (learnId,)
        keys = (('data', 'learnId'),)
        case = TestCaseAssembly().setAipParam('toPay',values,keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])


        '''提取参数learnId'''
        AfParamCom().moreParam(response.text, 'toPay', (('CStudent', 'feeList'),('CStudent', 'feeList')))



        resJosn = getJsonParm(response.text, 'body')
        learnId = str(resJosn['data'][0]['learnId']), ('data', 'learnId')
        BeParamCom().setLearn((('CJ', 'learnId'),), learnId)



    @unittest.skip("skipping")
    def test_7_cj_fd_pay(self):
        '''成教学员支付辅导费'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        '''提取到的'''
        unvsid = extFile.getYamlParms(('CStudent', 'unvsId'))
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        taId = extFile.getYamlParms(('CStudent', 'taId'))
        feeList = extFile.getYamlParms(('CStudent', 'feeList'))
        '''配置的'''
        scholarship = intFile.getYamlParms(('CJ', 'scholarships'))
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        grade = intFile.getYamlParms(('CJ', 'grade'))
        pfsnLevel = intFile.getYamlParms(('CJ', 'level'))
        mobile = BeParamCom().getPhone()
        idCard = BeParamCom().getCard()


        values = (str(unvsid),str(pfsnId),str(taId),str(feeList),str(scholarship),str(recruitType),str(grade),str(pfsnLevel),str(mobile),str(idCard))
        keys = (('data', 'unvsId'),('data', 'pfsnid'),('data', 'taId'),('data', 'feeList'),('data', 'scholarship')
                , ('data', 'recruitType'),('data', 'grade'),('data', 'pfsnLevel'),('data', 'mobile'),('data', 'idCard'))
        case = TestCaseAssembly().setAipParam('CrecruitAdd',values,keys)
        data = MultipartEncoder(fields=case[3])
        DataSource().setHearder(data.content_type)
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("regiester"), urls=case[2], data=data)
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)




    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
