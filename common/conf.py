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
        # self.f = self.path2 + "\\config\\application.yaml"
        self.f = self.path2 + "\\test_data\\regiester.yaml"
        self.h = self.path2 + "\\test_data\\Hearder.yaml"

    '''写入yaml文件'''
    def Wyaml(self,args):
        with open(self.f,'w',encoding='utf-8') as f:
            yaml.dump(args,f)

    '''取的hearder'''
    def Hyaml(self):
        with open(self.h,'r',encoding='utf-8') as f:
            return yaml.load(f,Loader=yaml.FullLoader).get('hearder')
    '''读取yaml文件'''
    def Ryaml(self):
        with open(self.f,'r',encoding='utf-8') as f:
            return yaml.load(f,Loader=yaml.FullLoader)

    def Upyaml(self,k,v):
        with open(self.f,'w',encoding="utf-8") as f:
            content = yaml.load(f,Loader=yaml.FullLoader)
            # r = content[k[0]]
            for i in k:
                content = content[k[i]]
            yaml.dump(content,f)


if __name__ == '__main__':
    i= Config()
    i.Upyaml(['regiester','test1','data','mobile'],155555555)
