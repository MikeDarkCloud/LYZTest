import requests
from common.Log import *
class YzApi:
    def __init__(self, url=None, data=None, headers=None):
        self.r = requests.session()
        self.log = Log()
        try:
            if url != None:
                self.r.post(url, data, headers)
        except   Exception as e:
            self.log.info(url + ":请求登录失败:" + e)
            # print(loginurl + ":请求登录失败:" + e)

    def lapi(self, method, urls, data=None, headers=None):
        if method == "post" or method == "POST":
            try:
                r = self.r.post(url=urls, data=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                self.log.info(urls + ":请求失败:" + e)
                # print(urls + ":请求失败:" + e)

        if method == "get" or method == "GET":
            try:
                r = self.r.get(url=urls, params=data, headers=headers)
                r.encoding = 'utf-8'
                return r
            except Exception as e:
                self.log.info(urls + ":请求失败:" + e)
                # print(urls + ":请求失败:" + e)


if __name__ == '__main__':
    '''调试'''
    print(YzApi('http://bms.yzwill.cn/loginByMobile.do',{'isOpenImage':'','mobile':13560148201,'ImgValidCode':'','validCode':888888}).lapi('post', 'http://bms.yzwill.cn/recruit/findRecruitStudents',{'start':0,'length':10,'loginName':'蓝明勇','recruitName':'蓝明勇'}).text)
