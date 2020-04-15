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
        intFile  = YamlParser('StudentInfo')
        case =TestCaseAssembly().setAipParam('getGkOpenEnrollCityInfo',(intFile.getYamlParms(('GK','grade')),intFile.getYamlParms(('GK','level'))),(('data','ext2'),('data','ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        rr= response.text
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response.text,'getGkOpenEnrollCityInfo',('GStudent','city'))

    @unittest.skip("skipping")
    def test_1_sUnvs(self):
        '''随机获取国开院校ID'''
        intFile  = YamlParser('StudentInfo')
        Para = {intFile.getYamlParms(('Gk','recruitType')):('data','ext1')}
        case =TestCaseAssembly().setAipParam('sUnvs',Para)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)
        '''提取参数'''
        AfParamCom().saveParam(response,'sUnvs',('GStudent','unvsId'))

    @unittest.skip("skipping")
    def test_2_getOpenTestAreaByCity(self):
        '''随机获取国开报读考区'''
        intFile  = YamlParser('StudentInfo')
        extFile  = YamlParser('LearnInfo')
        Para = {intFile.getYamlParms(('Gk','level')):('data','ext2')}
        Para.update({intFile.getYamlParms(('Gk', 'grade')): ('data', 'ext3')})
        Para.update({extFile.getYamlParms(('GStudent', 'city')): ('data', 'ext1')})
        case =TestCaseAssembly().setAipParam('getOpenTestAreaByCity',Para)
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)
        '''提取参数'''
        # AfParamCom().saveParam(response,'getOpenTestAreaByCity',(('GStudent','taId'),('GStudent','taName')))



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


    #创建数据
    # q=createTestdate()
    # i = 1
    # while(i > 0 ):
    #   q.createRegiesterTestdate()
    #   q.createGkRegiesterTestdate()
    #   i=i-1