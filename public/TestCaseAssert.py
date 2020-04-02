'''断言参数'''
from tools.Regular import *
class MyAssert():
    def __init__(self):
        pass

    def getAssert(self,content,patt):
        return regx(content,patt)


    def assertchar(self,context,k):
        isTrue = True
        for i in k:
            if i not in context:
                isTrue =isTrue and False
        return isTrue

if __name__ == '__main__':
    print(MyAssert().assertchar('11223344',['11','225']))