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
        # self.filename=os.listdir(self.path2+"\\test_data")
        # self.path2 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")

        self.f = self.path1 + "\\test_data\\regiester.yaml"
        self.h = self.path1 + "\\test_data\\Hearder.yaml"
        self.l = self.path1 + "\\test_data\\Logining.yaml"
        self.app = self.path1 + "\\config\\application.yaml"

    '''写入yaml文件'''
    def Wyaml(self,content):
        with open(self.f,'w',encoding='utf-8') as f:
            yaml.dump(content,f)

    '''读取yaml文件'''
    def Ryaml(self):
        with open(self.f,'r',encoding='utf-8') as f:
            return yaml.load(f)

    def Hyaml(self):
        with open(self.h,'r',encoding='utf-8') as f:
            return yaml.load(f)

    def Lyaml(self):
        with open(self.l,'r',encoding='utf-8') as f:
            return yaml.load(f)

    def path_log(self):
        with open(self.app,'r',encoding='utf-8') as f:
            p2=yaml.load(f)['path_log']
            path = os.path.join(self.path2, p2)
            return path
if __name__ == '__main__':
    print(os.listdir(os.path.dirname(os.path.abspath('.')) + "\\test_data"))

