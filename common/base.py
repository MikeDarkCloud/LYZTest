import requests
from common.Log import *
class YzApi():
    def __init__(self):
        y = Config()
        self.r = requests.session()
        self.log = Log()
        self.url='http://bms.yzwill.cn/loginByMobile.do'
        self.data = {'isOpenImage': '','mobile': 13560148201,'ImgValidCode': '','validCode': 888888}
        self.header = y.Hyaml()['hearder']

        try:
            if self.url != None:
                r = self.r.post(url=self.url, data=self.data,headers =self.header)
                print(r.text)
        except   Exception as e:
            self.log.info(self.url + ":请求登录失败:" + str(e))
            # print(loginurl + ":请求登录失败:" + e)

    def lapi(self, method, urls, data=None, headers=None):
        if method == "post" or method == "POST":
            try:
                r = self.r.post(url=urls, data=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                # self.log.info(urls + ":请求失败:" + str(e))
                print(urls + ":请求失败:" + str(e))

        if method == "get" or method == "GET":
            try:
                r = self.r.get(url=urls, params=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                self.log.info(urls + ":请求失败:" + str(e))
                # print(urls + ":请求失败:" + e)


if __name__ == '__main__':
    '''调试'''
    print(YzApi('http://bms.yzwill.cn/loginByMobile.do',{'isOpenImage':'','mobile':13560148201,'ImgValidCode':'','validCode':888888}).lapi('post', 'http://bms.yzwill.cn/recruit/findRecruitStudents',{'start':0,'length':10,'loginName':'蓝明勇','recruitName':'蓝明勇'}).text)
