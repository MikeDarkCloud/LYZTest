from common.base import *
from public.TestCaseAssembly import TestCaseAssembly
from public.TestCaseAssert import *

class createTestdate():
    def __init__(self):
        self.log = Log()
        self.r = YzApi()
    '''生成测试数据'''
    def createRegiesterTestdate(self):
        case = TestCaseAssembly().getRegisterTestCaseData(self.r,'regiester')
        response = self.r.lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response.text)
        print(MyAssert().assertchar(response.text,['true','00']))

    def createGkRegiesterTestdate(self):
        case = TestCaseAssembly().getRegisterTestCaseData(self.r,'Gkregiester')
        response = self.r.lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        self.log.info(response.text)
        print(MyAssert().assertchar(response.text,['true','00']))



if __name__ == '__main__':
    q=createTestdate()
    i = 10
    while(i > 0 ):
      q.createRegiesterTestdate()
      q.createGkRegiesterTestdate()
      i=i-1
