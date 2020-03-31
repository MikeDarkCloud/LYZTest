'''断言参数'''
from tools.Regular import *
class MyAssert():
    def __init__(self):
        pass

    def getAssert(self,content,patt):
        return regx(content,patt)


    def assertchar(self,context,k):
        if k in context:
            return True
        else:
            return False
