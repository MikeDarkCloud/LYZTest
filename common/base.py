import requests
from common.Log import *
from common.DataSource import *


class YzApi():
    def __init__(self):
        self.DataSource = DataSource()
        self.Yaml = self.DataSource.getRallyaml('Logining')
        self.log = Log()

    def login(self):
        try:
            if self.Yaml.get('urls') != None:
                r = requests.session().post(url=self.DataSource.getBaseUrl() + self.Yaml.get('urls'),
                                            data=self.Yaml.get('data'), headers=self.DataSource.getHearder('login'))
                self.DataSource.setCookie(requests.utils.dict_from_cookiejar(r.cookies))
                self.log.info('post' + ' ' + 'logining success!')
        except Exception as e:
            self.log.info(self.DataSource.getBaseUrl() + self.Yaml.get('urls') + ":请求登录失败:" + str(e))

    def lapi(self, method, urls, data=None, headers=None, json=None):
        if method == "post" or method == "POST":
            try:
                r = requests.post(url=self.DataSource.getBaseUrl() + urls, json=json, data=data, headers=headers,
                                  cookies=self.DataSource.getCookie())
                p = r
                r.encoding = 'utf-8'
                self.log.info(method + ' ' + self.DataSource.getBaseUrl() + urls + ":请求发送成功！")
                return r
            except Exception as e:
                self.log.info(method + ' ' + self.DataSource.getBaseUrl() + urls + ":请求失败:" + str(e))

        if method == "get" or method == "GET":
            try:
                r = requests.get(url=self.DataSource.getBaseUrl() + urls, params=data, headers=headers,
                                 cookies=self.DataSource.getCookie())
                r.encoding = 'utf-8'
                self.log.info(method + ' ' + self.DataSource.getBaseUrl() + urls + ":请求发送成功！")
                return r
            except Exception as e:
                self.log.info(method + self.DataSource.getBaseUrl() + urls + ":请求失败:" + str(e))

    def getBaseinfo(self, type):
        try:
            i = True
            while (i):
                if type == 'idCard':
                    url = self.Yaml.get('IDurl')
                    data = {'stdName': '', 'idCard': self.DataSource.getIdcard(), 'idType': 1, 'recruitType': 1}
                if type == 'mobile':
                    url = self.Yaml.get('MOurl')
                    data = {'mobile': self.DataSource.getMobile()}
                r = requests.post(url=self.DataSource.getBaseUrl() + url, data=data, headers=self.Yaml.get('hearders'),
                                  cookies=self.DataSource.getCookie())
                r.encoding = 'utf-8'
                if 'true' in r.text or 'E000034' in r.text:
                    i = False
            return data[type]
        except Exception as e:
            self.log.info(self.DataSource.getBaseUrl() + ":请求失败:" + str(e))


if __name__ == '__main__':
    '''调试'''
    t = YzApi()
    t.log.info('aaaaaaaaaaaaaa')
    # self.w = Config().Rallyaml('Logining')
    # cookies = self.y['Cookie']
    #
