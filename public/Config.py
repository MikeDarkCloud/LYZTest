# -*-coding:utf-8-*-
'''
配置文件--配置公共参数
'''
import os
import yaml


class Config:
    def __init__(self):
        self.path1 = os.getcwd()
        self.path2 = os.path.dirname(os.path.abspath('.'))
        # self.path2 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        file_path = self.path2 + "\\conf\\conf.yml"
        with open(str(file_path),"a+",encoding='utf-8') as file:
            self.file = yaml.load(file)


    def setUrl(self):
        yaml.dump({"cii":44},self.file)


if __name__ == '__main__':
    i= Config()
    print(i.setUrl())
