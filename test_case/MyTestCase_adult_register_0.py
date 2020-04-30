from common.myunit import *
from ddt import ddt, data, unpack
from public.TestCaseAssembly import TestCaseAssembly, BeforeParamCom
from public.TestCaseAssert import MyAssert
from public.YamlParser import *
from public.AfterParamCom import *
from requests_toolbelt import MultipartEncoder


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
        AfterParamCom().saveParam(response.text, 'sUnvs', ('CStudent', 'unvsId'))

    # @unittest.skip("skipping")
    def test_1_sPfsnByOnScholarship(self):
        '''随机获取成教专业'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        grade = intFile.getYamlParms(('CJ', 'grade'))
        level = intFile.getYamlParms(('CJ', 'level'))
        sId = extFile.getYamlParms(('CStudent', 'unvsId'))
        values = (grade, level, sId)
        keys = (('data', 'ext2'), ('data', 'ext1'), ('data', 'sId'))
        case = TestCaseAssembly().setAipParam('sPfsnByOnScholarship', values, keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True,)
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'sPfsnByOnScholarship', ('CStudent', 'pfsnId'))

    # @unittest.skip("skipping")
    def test_2_getOpenTestAreaByCity(self):
        '''随机获取考区'''
        extFile = YamlParser('LearnInfo')
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        values = (pfsnId,)
        keys = (('data', 'sId'),)
        case = TestCaseAssembly().setAipParam('sTaNotStop', values, keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'sTaNotStop', ('CStudent', 'taId'))

    # @unittest.skip("skipping")
    def test_3_showFeeList(self):
        '''获取收费标准'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        taId = extFile.getYamlParms(('CStudent', 'taId'))
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        scholarship = intFile.getYamlParms(('CJ', 'scholarships'))
        values = (pfsnId, taId, recruitType, scholarship)
        keys = (('data', 'pfsnId'), ('data', 'taId'), ('data', 'recruitType'), ('data', 'scholarship'))
        case = TestCaseAssembly().setAipParam('showFeeList', values, keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'showFeeList', ('CStudent', 'feeList'))

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
        mobile = BeforeParamCom().getPhone()
        idCard = BeforeParamCom().getCard()
        self.log.info('学员手机号：'+mobile)
        self.log.info('学员身份证号：'+idCard)
        BeforeParamCom().setLearn((('CStudent', 'mobile'),), mobile)
        BeforeParamCom().setLearn((('CStudent', 'idCard'),), idCard)
        values = (str(unvsid), str(pfsnId), str(taId), str(feeList), str(scholarship), str(recruitType), str(grade), str(pfsnLevel), str(mobile), str(idCard))
        keys = (('data', 'unvsId'), ('data', 'pfsnid'), ('data', 'taId'), ('data', 'feeList'), ('data', 'scholarship')
                , ('data', 'recruitType'), ('data', 'grade'), ('data', 'pfsnLevel'), ('data', 'mobile'), ('data', 'idCard'))
        case = TestCaseAssembly().setAipParam('CrecruitAdd', values, keys)
        data = MultipartEncoder(fields=case[3])
        DataSource().setHearder(data.content_type)
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("regiester"), urls=case[2], data=data)
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_5_stdFeeList(self):
        '''财务管理搜索结果获取learn_id'''
        extFile = YamlParser('LearnInfo')
        mobile = extFile.getYamlParms(('CStudent', 'mobile'))
        values = (mobile,)
        keys = (('data', 'mobile'),)
        case = TestCaseAssembly().setAipParam('stdFeeList', values, keys)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数learnId'''
        resJosn = getJsonParm(response.text, 'body')
        learnId = str(resJosn['data'][0]['learnId'])
        BeforeParamCom().setLearn((('CStudent', 'learnId'),), learnId)
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_6_toPay(self):
        '''获取支付订单及web_token'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        case = TestCaseAssembly().setAipParam('toPay', (learnId,), (('data', 'learnId'),))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数learnId'''
        AfterParamCom().moreParam(response.text, 'toPay', (('CStudent', 'order'), ('CStudent', '_web_token')))
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_7_cj_fd_pay(self):
        '''成教学员支付辅导费(不使用抵扣)'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        '''提取到的'''
        order = extFile.getYamlParms(('CStudent', 'order'))
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        web_token = extFile.getYamlParms(('CStudent', '_web_token'))
        tutorPayInfos = getJsonParm(order, 'tutorPayInfos')[0]
        payAmount = payableCount = amount = tutorPayInfos['payable']
        itemName = tutorPayInfos['itemName']
        orderNo = tutorPayInfos['subOrderNo']
        paymentType = 1
        '''配置的'''
        grade = intFile.getYamlParms(('CJ', 'grade'))
        values = (str(learnId), str(learnId), str(web_token), str(grade), str(grade), str(payableCount), str(payAmount), str(amount),
                  str(itemName), str(orderNo), str(paymentType))
        keys = (('data', 'learnId'), ('data', 'payData', 'learnId'), ('data', '_web_token'), ('data', 'grade'),
                ('data', 'payData', 'grade'), ('data', 'payableCount'), ('data', 'payData', 'payAmount'), ('data', 'payData', 'items', 0, 'amount'),
                ('data', 'payData', 'items', 0, 'itemName'), ('data', 'payData', 'items', 0, 'orderNo'), ('data',  'paymentType'))

        case = TestCaseAssembly().setAipParam('pay', values, keys)
        case[3]['payData']=str(case[3]['payData'])
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("PHearder"), urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数:subOrderNo'''
        DataSource().setLearnInfo('CStudent','subOrderNo',orderNo)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
