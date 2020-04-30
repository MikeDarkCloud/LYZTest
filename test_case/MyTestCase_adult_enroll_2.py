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
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
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
        '''提取参数learnId+web_token'''
        AfterParamCom().moreParam(response.text, 'toPay', (('CStudent', 'order'), ('CStudent', '_web_token')))
        '''断言'''
        # self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

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
        values = (str(learnId), str(learnId), str(web_token), str(grade), str(grade), str(payableCount), str(payAmount),str(payAmount), str(amount),
                  str(itemName), str(orderNo), str(paymentType))
        keys = (('data', 'learnId'), ('data', 'payData', 'learnId'), ('data', '_web_token'), ('data', 'grade'),
                ('data', 'payData', 'grade'), ('data', 'payableCount'), ('data', 'payData', 'payAmount'),('data', 'payData', 'items',0,'payAmount'), ('data', 'payData', 'items', 0, 'amount'),
                ('data', 'payData', 'items', 0, 'itemName'), ('data', 'payData', 'items', 0, 'orderNo'), ('data',  'paymentType'))

        case = TestCaseAssembly().setAipParam('pay', values, keys)
        case[3]['payData']=str(case[3]['payData'])
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("PHearder"), urls=case[2], data=case[3])
        '''提取参数:subOrderNo'''
        DataSource().setLearnInfo('CStudent','subOrderNo',orderNo)
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_8_reviewFee(self):
        '''成教学员辅导费缴费审核'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        subOrderNo = extFile.getYamlParms(('CStudent', 'subOrderNo'))
        case = TestCaseAssembly().setAipParam('reviewFee', (learnId,subOrderNo), (('data', 'learnId'),('data', 'subOrderNo')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @unittest.skip("skipping")
    def test_9_getAnnexList(self):
        '''成教学员获取附件ID'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        case = TestCaseAssembly().setAipParam('getAnnexList', (learnId,recruitType), (('data', 'learnId'),('data', 'recruitType')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数annexId'''
        resJosn = getJsonParm(response.text, 'body')
        annexId1 = resJosn['data'][0]['annexId']
        annexId2 = resJosn['data'][1]['annexId']
        annexId3 = resJosn['data'][2]['annexId']
        annexId4 = resJosn['data'][3]['annexId']
        BeforeParamCom().setLearn((('CStudent', 'annexId1'),), annexId1)
        BeforeParamCom().setLearn((('CStudent', 'annexId2'),), annexId2)
        BeforeParamCom().setLearn((('CStudent', 'annexId3'),), annexId3)
        BeforeParamCom().setLearn((('CStudent', 'annexId4'),), annexId4)

    # @unittest.skip("skipping")
    def test_A_updateAnnex(self):
        '''成教学员上传附件'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        annexId1 = extFile.getYamlParms(('CStudent', 'annexId1'))
        annexId2 = extFile.getYamlParms(('CStudent', 'annexId2'))
        annexId3 = extFile.getYamlParms(('CStudent', 'annexId3'))
        annexId4 = extFile.getYamlParms(('CStudent', 'annexId4'))
        annexId = [annexId1,annexId2,annexId3,annexId4]
        annexType = [1,2,3,4]
        annexName = ['身份证正面照','身份证背面照','学历证书','相片']
        assert0 = True
        for i in annexId:
            case = TestCaseAssembly().setAipParam('updateAnnex', (i,learnId,annexType[annexId.index(i)],annexName[annexId.index(i)]),
                                                 (('data', 'annexId'),('data', 'learnId'),('data', 'annexType'),('data', 'annexName')))
            data0 = {'annexFile':('1.jpg',open('C:\\YZeducation\\PyProject\\LYZTest\\test_data\\image\\1.jpg','rb'),'image/jpeg'),
                     'annexId':str(i),
                     'annexName':annexName[annexId.index(i)],
                     'annexType':str(annexType[annexId.index(i)]),
                     'annexUrl': '',
                     'isRequire':'1',
                     'learnId':str(learnId)}
            data = MultipartEncoder(fields=data0)
            DataSource().setHearder(data.content_type)
            response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("regiester"), urls=case[2], data=data)
            assert1=MyAssert().assertchar(response.text, ['true', '00'])
            assert0 = assert0 and assert1
        '''断言'''
        self.assertTrue(assert0, True)

    # @unittest.skip("skipping")
    def test_B_getCommonAnnexList(self):
        '''成教学员获取附件审核crId'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'idCard'))
        case = TestCaseAssembly().setAipParam('getCommonAnnexList', (learnId,), (('data', 'idCard'),))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数crId'''
        AfterParamCom().saveParam(response.text, 'getCommonAnnexList', ('CStudent', 'crId'))

    def test_C_annexCheck(self):
        '''成教学员附件审核-总审'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        recruitType = intFile.getYamlParms(('CJ', 'recruitType'))
        crId = extFile.getYamlParms(('CStudent', 'crId'))
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        case = TestCaseAssembly().setAipParam('annexCheck', (crId,recruitType,learnId), (('data', 'crId'),('data', 'recruitType'),('data', 'learnId')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    def test_D_annexCheckCharge(self):
        '''成教学员附件审核-附件审核'''
        extFile = YamlParser('LearnInfo')
        annexId1 = extFile.getYamlParms(('CStudent', 'annexId1'))
        annexId2 = extFile.getYamlParms(('CStudent', 'annexId2'))
        annexId3 = extFile.getYamlParms(('CStudent', 'annexId3'))
        annexId4 = extFile.getYamlParms(('CStudent', 'annexId4'))
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        annexId = [annexId1,annexId2,annexId3,annexId4]
        assert0 = True
        for i in annexId:
            case = TestCaseAssembly().setAipParam('annexCheckCharge', (i,learnId), (('data', 'annexId'),('data', 'learnId')))
            response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
            assert1 = MyAssert().assertchar(response.text, ['true', '00'])
            assert0 =assert0 and assert1
        '''断言'''
        self.assertTrue(assert0, True)

    def test_E_testConfirm_okConfirm(self):
        '''成教学员考前确认'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        case = TestCaseAssembly().setAipParam('okConfirm', (learnId,), (('data', 'learnId'),))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    def test_F_studentScore_edit(self):
        '''成教学员获取入学考试成绩录入web_token'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        idCard = extFile.getYamlParms(('CStudent', 'idCard'))
        case = TestCaseAssembly().setAipParam('studentScore_edit', (learnId,idCard), (('data', 'learnId'),('data', 'idCard')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['_web_token']), True)
        '''提取参数courses+web_token'''
        AfterParamCom().moreParam(response.text, 'studentScore_edit', (('CStudent', '_web_token'), ('CStudent', 'courses')))

    def test_I_updateStudentScore(self):
        '''成教学员入学考试成绩录入'''
        extFile = YamlParser('LearnInfo')
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        web_token = extFile.getYamlParms(('CStudent', '_web_token'))
        courses = extFile.getYamlParms(('CStudent', 'courses'))
        param = getJsonParm(courses)
        courseId0 = param[0]['subjectId']
        courseName0=param[0]['subjectName']
        courseId1 = param[1]['subjectId']
        courseName1=param[1]['subjectName']
        courseId2 = param[2]['subjectId']
        courseName2=param[2]['subjectName']

        case = TestCaseAssembly().setAipParam('updateStudentScore', (learnId,web_token,courseId0,courseName0,courseId1,courseName1,courseId2,courseName2),
                                              (('data', 'learnId'),('data', '_web_token'),('data', 'scores[0].courseId'),('data', 'scores[0].courseName'),
                                               ('data', 'scores[1].courseId'), ('data', 'scores[1].courseName'),('data', 'scores[2].courseId'),('data', 'scores[2].courseName')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    def test_J_stdEnroll_enroll(self):
        '''成教学员录取'''
        extFile = YamlParser('LearnInfo')
        intFile = YamlParser('StudentInfo')
        level = intFile.getYamlParms(('CJ', 'level'))
        learnId = extFile.getYamlParms(('CStudent', 'learnId'))
        grade = intFile.getYamlParms(('CJ', 'grade'))
        pfsnId = extFile.getYamlParms(('CStudent', 'pfsnId'))
        unvsId = extFile.getYamlParms(('CStudent', 'unvsId'))

        case = TestCaseAssembly().setAipParam('stdEnroll', (learnId,level,grade,pfsnId,unvsId),
                                              (('data', 'learnId'),('data', 'level'),('data', 'grade'),('data', 'pfsnId'),('data', 'unvsId')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''断言'''
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

