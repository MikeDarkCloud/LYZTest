import requests
from common.Log import *
from tools.CreateIdentity import *
from tools.CreateMobile import *


class YzApi():
    def __init__(self):
        self.y = Config().Rallyaml('Logining')
        self.r = requests.session()
        self.log = Log()
        try:
            if self.y['urls'] != None:
                self.r.post(url=self.y['urls'], data=self.y['data'], headers=self.y['hearder'])
                self.log.info('logining success!')
        except Exception as e:
            self.log.info(self.y['urls'] + ":请求登录失败:" + str(e))

    def lapi(self, method, urls, data=None, headers=None):
        if method == "post" or method == "POST":
            try:
                r = self.r.post(url=urls, data=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                self.log.info(urls + ":请求失败:" + str(e))

        if method == "get" or method == "GET":
            try:
                r = self.r.get(url=urls, params=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                self.log.info(urls + ":请求失败:" + str(e))

    def getBaseinfo(self, type):
        try:
            i = True
            while (i):
                if type == 'idCard':
                    url = self.y['IDurl']
                    data = {'stdName': '', 'idCard': create_identity(int(area_dict1), 22, 1), 'idType': 1, 'recruitType': 1}
                if type == 'mobile':
                    url = self.y['MOurl']
                    data = {'mobile': get_mobile()}
                r = self.r.post(url=url, data=data, headers=self.y['hearder'])
                r.encoding = 'utf-8'
                if 'true' in r.text:
                    i = False
            return data[type]
        except Exception as e:
            self.log.info(":请求失败:" + str(e))


if __name__ == '__main__':
    '''调试'''
    t = YzApi()
    t.log.info('aaaaaaaaaaaaaa')
