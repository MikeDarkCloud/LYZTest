from CreateTestDate import createTestdate
from common.myunit import *
from ddt import ddt, data, unpack

from public.TestCaseAssembly import TestCaseAssembly
from public.TestCaseAssert import MyAssert


# @ddt
class MyTestCase(StartEnd):

    def setUp(self):
        pass

    # @ddt()
    def test_normal_register(self):
        '''随机录入成教类型学员学员'''
        case =TestCaseAssembly().getRegisterTestCaseData('CrecruitAdd')
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response.text)
        self.assertTrue(MyAssert().assertchar(response.text,['true','00']), True)

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