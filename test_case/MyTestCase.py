from common.myunit import *
from ddt import ddt, data, unpack
from public.TestCaseAssembly import TestCaseAssembly
from public.TestCaseAssert import MyAssert
from public.YamlParser import *
from public.AfParamCom import *


# @ddt
class MyTestCase(StartEnd):

    def setUp(self):
        pass

    def test_0_getGkOpenEnrollCityInfo(self):
        '''随机获取国开报读城市'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('getGkOpenEnrollCityInfo', (intFile.getYamlParms(('GK', 'grade')), intFile.getYamlParms(('GK', 'level'))),
                                              (('data', 'ext2'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'getGkOpenEnrollCityInfo', ('GStudent', 'city'))

    # @unittest.skip("skipping")
    def test_1_sUnvs(self):
        '''随机获取国开院校ID'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('sUnvs', intFile.getYamlParms(('GK', 'recruitType')), ('data', 'ext1'))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'sUnvs', ('GStudent', 'unvsId'))

    # @unittest.skip("skipping")
    def test_2_getOpenTestAreaByCity(self):
        '''随机获取国开报读考区ID+考区名称'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenTestAreaByCity', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'city'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'getOpenTestAreaByCity', (('GStudent', 'taId'), ('GStudent', 'taName')))

    # @unittest.skip("skipping")
    def test_3_getOpenPfsnByTaId(self):
        '''随机获取国开报读专业pfsnId+专业名称pfsnName+专业编号pfsnCode'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenPfsnByTaId', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'taId'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text, 'getOpenPfsnByTaId', (('GStudent', 'pfsnId'), ('GStudent', 'pfsnName'), ('GStudent', 'pfsnCode')))

    def test_4_showFeeList(self):
        '''获取国开报读收费标准信息'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('showFeeList', (
        intFile.getYamlParms(('GK', 'recruitType')), intFile.getYamlParms(('GK', 'scholarships')), extFile.getYamlParms(('GStudent', 'pfsnId')),
        extFile.getYamlParms(('GStudent', 'taId'))), (('data', 'recruitType'), ('data', 'scholarship'), ('data', 'pfsnId'), ('data', 'taId')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)
        '''提取参数'''
        AfParamCom().saveJson(response.text, (('body','feeInfo','feeId'),('body','feeList')), (('GStudent', 'feeId'),('GStudent', 'feeList')))

    @unittest.skip("skipping")
    def test_5_gk_normal_register(self):
        '''随机录入国开类型学员学员'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        '''从配置文件获取'''
        grade = intFile.getYamlParms(('GK', 'grade'))
        recruitType = intFile.getYamlParms(('GK', 'recruitType'))
        scholarship = intFile.getYamlParms(('GK', 'scholarships'))
        '''从参数文件获取'''
        city = extFile.getYamlParms(('GStudent', 'city'))
        feeList = extFile.getYamlParms(('GStudent', 'feeList'))
        pfsnCode = extFile.getYamlParms(('GStudent', 'pfsnCode'))
        pfsnId = extFile.getYamlParms(('GStudent', 'pfsnId'))
        pfsnName = extFile.getYamlParms(('GStudent', 'pfsnName'))
        taId = extFile.getYamlParms(('GStudent', 'taId'))
        taName = extFile.getYamlParms(('GStudent', 'taName'))
        unvsId = extFile.getYamlParms(('GStudent', 'unvsId'))
        '''将参数组合到接口文件'''
        case = TestCaseAssembly().setAipParam('showFeeList', ('', '', '',''), (('data', 'recruitType'), ('data', 'scholarship'), ('data', 'pfsnId'), ('data', 'taId')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text, ['true', '00']), True)

    # @ddt()
    # def test_0_cj_normal_register(self):
    #     '''随机录入成教类型学员学员'''
    #     case =TestCaseAssembly().getAipParam('CrecruitAdd')
    #     response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
    #     self.log.info(response.text)
    #     self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)

    # # @unittest.skip("skipping")
    # def test_1_gk_normal_register(self):
    #     '''随机录入国开类型学员学员'''
    #     case =TestCaseAssembly().getRegisterTestCaseData('GrecruitAdd')
    #     response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
    #     self.log.info(response.text)
    #     self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)
    #
    # # @unittest.skip("skipping")
    # def test_2_cj_fd_pay(self):
    #     '''成教学员支付辅导费'''
    #     case = TestCaseAssembly().getPayData()
    #     response0 = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
    #     self.log.info(response0.text)
    #     self.assertTrue(MyAssert().assertchar(response0.text,['true','00']), True)
    #
    # def test_3_gk_xk_pay(self):
    #     pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

    # 创建数据
    # q=createTestdate()
    # i = 1
    # while(i > 0 ):
    #   q.createRegiesterTestdate()
    #   q.createGkRegiesterTestdate()
    #   i=i-1
