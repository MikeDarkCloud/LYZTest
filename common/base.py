import requests
from common.Log import *
from tools.CreateIdentity import *
from tools.CreateMobile import *


class YzApi():
    def __init__(self):
        y = Config()
        self.r = requests.session()
        self.log = Log()
        self.IDurl = y.Lyaml()['IDurl']
        self.MOurl = y.Lyaml()['MOurl']
        self.url = y.Lyaml()['urls']
        self.data = y.Lyaml()['data']
        self.header = y.Hyaml()['hearder']

        try:
            if self.url != None:
                r = self.r.post(url=self.url, data=self.data, headers=self.header)
                self.log.info('loging success!')
        except Exception as e:
            self.log.info(self.url + ":请求登录失败:" + str(e))

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
                    url = self.IDurl
                    data = {'stdName': '', 'idCard': create_identity(int(area_dict1), 22, 1), 'idType': 1, 'recruitType': 1}
                if type == 'mobile':
                    url = self.MOurl
                    data = {'mobile': get_mobile()}
                r = self.r.post(url=url, data=data, headers=self.header)
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
