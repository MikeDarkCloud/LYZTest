from common.base import *
from public.TestCaseAssembly import TestCaseAssembly
from public.TestCaseAssert import *

class createTestdate():
    def __init__(self):
        self.r = YzApi()
    '''生成测试数据'''
    def createRegiesterTestdate(self):
        case = TestCaseAssembly().getRegisterTestCaseData(self.r,'regiester')
        response = self.r.lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        print(MyAssert().assertchar(response.text,'true'))

    def createGkRegiesterTestdate(self):
        case = TestCaseAssembly().getRegisterTestCaseData(self.r,'Gkregiester')
        response = self.r.lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        print(MyAssert().assertchar(response.text,'true'))



if __name__ == '__main__':
    q=createTestdate()
    i = 1
    while(i > 0 ):
      # r = q.createRegiesterTestdate()
      r = q.createGkRegiesterTestdate()
      i=i-1
