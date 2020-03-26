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
        self.f = self.path2 + "\\config\\application.yaml"

    '''写入yaml文件'''
    def Wyaml(self,args):
        with open(self.f,'w',encoding='utf-8') as f:
            yaml.dump(args,f)


    def Ryaml(self):
        with open(self.f,'r',encoding='utf-8') as f:
            return yaml.load(f,Loader=yaml.FullLoader)

if __name__ == '__main__':
    i= Config()
    print(i.Ryaml().get('bb'))
