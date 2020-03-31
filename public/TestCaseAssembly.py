from requests_toolbelt import MultipartEncoder
from common.conf import Config


class TestCaseAssembly():

    def __init__(self):
        # self.y = Config().Rallyaml('regiester')
        pass


    def getRegisterTestCaseData(self,r,casefile):
        y = Config().Rallyaml(casefile)
        y['data']['idCard'] = r.getBaseinfo('idCard')
        y['data']['mobile'] = r.getBaseinfo('mobile')
        data = MultipartEncoder(fields=y['data'])
        y['hearder']['Content-Type'] = data.content_type
        headers = y['hearder']
        method = y['method']
        urls = y['urls']
        return method,headers,urls,data

    def getPay(self):
        pass





