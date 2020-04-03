import requests
from common.Log import *
from tools.CreateIdentity import *
from tools.CreateMobile import *


class YzApi():
    def __init__(self):
        self.y = Config().Rallyaml('Logining')
        self.w = Config()
        self.log = Log()

    def login(self):
        try:
            if self.y['urls'] != None:
                r=requests.session().post(url=self.y['urls'], data=self.y['data'], headers=self.y['hearders'])
                self.y['Cookie'] = requests.utils.dict_from_cookiejar(r.cookies)
                self.w.Wyaml(self.y,'Logining')
                self.log.info('post'+' '+'logining success!')
        except Exception as e:
            self.log.info(self.y['urls'] + ":请求登录失败:" + str(e))

    def lapi(self, method, urls, data=None, headers=None):
        if method == "post" or method == "POST":
            try:
                r = requests.post(url=urls, data=data, headers=headers,cookies = self.y['Cookie'])
                r.encoding = 'utf-8'
                self.log.info(method+' '+urls + ":请求发送成功！")
                return r
            except Exception as e:
                self.log.info(method+' '+urls + ":请求失败:" + str(e))

        if method == "get" or method == "GET":
            try:
                r = requests.get(url=urls, params=data, headers=headers,cookies = self.y['Cookie'])
                r.encoding = 'utf-8'
                self.log.info(method+' '+urls + ":请求发送成功！")
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
                r = requests.post(url=url, data=data, headers=self.y['hearders'],cookies = self.y['Cookie'])
                r.encoding = 'utf-8'
                if 'true' in r.text or 'E000034' in r.text:
                    i = False
            return data[type]
        except Exception as e:
            self.log.info(":请求失败:" + str(e))


if __name__ == '__main__':
    '''调试'''
    t = YzApi()
    t.log.info('aaaaaaaaaaaaaa')
    #self.w = Config().Rallyaml('Logining')
    # cookies = self.y['Cookie']
    #