from common.base import *
from public.TestCaseAssembly import TestCaseAssembly


class createTestdate():
    '''生成测试数据'''
    def createRegiesterTestdate(self):
        r = YzApi()
        case = TestCaseAssembly().getRegisterTestCaseData(r)
        qq = r.lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        print(qq.text)
if __name__ == '__main__':
    q=createTestdate()
    i = 1
    while(i > 0 ):
      r = q.createRegiesterTestdate()
      i=i-1
