from common.myunit import *
import ddt

@ddt.ddt
class Test(StartEnd):
    parm = {'www':111,'rrr':333}
    # @unittest.skip('skip this  case')
    # @ddt.file_data('TestYaml/testdata.yaml')
    # def setUp(self):
    #     pass
    @ddt.data(*parm)
    def test(self,args):
        '''testing'''
        print(args)
        self.assertEqual(args,args)
        # print(StartEnd().r)
        # k = kwargs.get("bmslogin")

        # response = YzApi().lapi(k)
        # self.assertEqual(response.status_code, 200, msg="后台登录接口异常！")
        # self.assertEqual(response.code_text, '{"code":"00","body":"SUCCESS","msg":"","ok":true}', msg="后台登录接口异常！失败！")
    #
    # def tearDown(self):
    #     pass


if __name__ == '__main__':
    unittest.main