from requests_toolbelt import MultipartEncoder

from common.myunit import *
import ddt


@ddt
class RegiesterTest(StartEnd):

    # @unittest.skip('skip this  case')
    # @ddt.file_data([{'ww':1},{'ee':2}])
    @ddt.data([{'ww':1},{'ee':2}])
    def test_regiester_case(self,**kwargs):
        '''testing test_regiester_case'''
        print(kwargs.get('ww'))
        # print(kwargs)
        # r = YzApi()
        # y = Config()
        # t = y.Ryaml()
        # t['data']['idCard'] = r.getBaseinfo('idCard')
        # t['data']['mobile'] = r.getBaseinfo('mobile')
        # m = MultipartEncoder(fields=t['data'])
        # t['hearder']['Content-Type'] = m.content_type
        # qq=r.lapi(method= t['method'],urls=t['urls'],data=m,headers=t['hearder'])





