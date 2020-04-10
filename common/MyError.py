class MyError(Exception):
    def isNoneError(self,value):
        if value == None:
            raise Exception("获取的参数为空！")


