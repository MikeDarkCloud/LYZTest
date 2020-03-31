from requests_toolbelt import MultipartEncoder
from common.conf import Config


class TestCaseAssembly():

    def __init__(self):
        self.y = Config().Ryaml()


    def getRegisterTestCaseData(self,r):
        self.y['data']['idCard'] = r.getBaseinfo('idCard')
        self.y['data']['mobile'] = r.getBaseinfo('mobile')
        data = MultipartEncoder(fields=self.y['data'])
        self.y['hearder']['Content-Type'] = data.content_type
        headers = self.y['hearder']
        method = self.y['method']
        urls = self.y['urls']
        return method,headers,urls,data

    def getPay(self):
        pass





