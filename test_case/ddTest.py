from public.myunit import *
import ddt
from public.base import *
@ddt
class ddTest(StartEnd):

    # @unittest.skip('skip this  case')
    ddt.file_data('TestYaml/testdata.yaml')
    def test_case(self,**kwargs):
        '''testing'''
        k = kwargs.get("bmslogin")

        # response = YzApi().lapi(k)
        # self.assertEqual(response.status_code, 200, msg="后台登录接口异常！")
        # self.assertEqual(response.code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="后台登录接口异常！失败！")




# if __name__ == '__main__':
#     ddTest().test_case()