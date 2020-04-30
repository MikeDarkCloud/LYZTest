'''
@description:自定义断言
@author:lanmingyong
'''
from tools.Regular import *
class MyAssert():
    def __init__(self):
        pass

    def getAssert(self,content,patt):
        '''正则匹配断言'''
        return regx(content,patt)


    def assertchar(self,context,k):
        '''关键字断言'''
        isTrue = True
        for i in k:
            if i not in context:
                isTrue =isTrue and False
        return isTrue

if __name__ == '__main__':
    print(MyAssert().assertchar('11223344',['11','225']))