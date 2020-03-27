from common.myunit import *
import ddt


@ddt
class RegiesterTest(StartEnd):

    # @unittest.skip('skip this  case')
    @ddt.file_data('TestYaml/testdata.yaml')
    def test_case(self,**kwargs):
        '''testing'''
        k = kwargs.get("bmslogin")
