from requests_toolbelt import MultipartEncoder
from common.base import *
class createTestdate():
    '''生成测试数据'''
    def createRegiesterTestdate(self):
        r = YzApi()
        y = Config()
        t = y.Ryaml()
        t['data']['idCard'] = r.getBaseinfo('idCard')
        t['data']['mobile'] = r.getBaseinfo('mobile')
        m = MultipartEncoder(fields=t['data'])
        t['hearder']['Content-Type'] = m.content_type
        qq=r.lapi(method= t['method'],urls=t['urls'],data=m,headers=t['hearder'])
        print(qq.text)
if __name__ == '__main__':
    q=createTestdate()
    i = 1
    while(i > 0 ):
      r = q.createRegiesterTestdate()
      i=i-1
