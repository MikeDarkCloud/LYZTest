from common.myunit import *
from ddt import ddt, data, unpack
from public.TestCaseAssembly import TestCaseAssembly
from public.TestCaseAssert import MyAssert


# @ddt
class MyTestCase(StartEnd):

    def setUp(self):
        pass

    # @ddt()
    def test_0_cj_normal_register(self):
        '''随机录入成教类型学员学员'''
        case =TestCaseAssembly().getRegisterTestCaseData('CrecruitAdd')
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response.text)
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)

    # @unittest.skip("skipping")
    def test_1_gk_normal_register(self):
        '''随机录入国开类型学员学员'''
        case =TestCaseAssembly().getRegisterTestCaseData('GrecruitAdd')
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response.text)
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)

    # @unittest.skip("skipping")
    def test_2_cj_fd_pay(self):
        '''成教学员支付辅导费'''
        case = TestCaseAssembly().getPayData()
        response0 = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response0.text)
        self.assertTrue(MyAssert().assertchar(response0.text,['true','00']), True)

    def test_3_gk_xk_pay(self):
        pass




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