# -*-coding:utf-8-*-
'''
配置文件--配置公共参数
'''
import os
import yaml

class Config:
    def __init__(self):
        self.dirdict={}
        self.path1 = os.getcwd()
        self.path2 = os.path.dirname(os.path.abspath('.'))
        self.app = self.path1 + "\\config\\application.yaml"
        # self.f = os.walk(os.path.dirname(os.path.abspath('.')) + "\\test_data", topdown=True, onerror=None, followlinks=False)
        self.f = os.walk(os.getcwd() + "\\test_data", topdown=True, onerror=None, followlinks=False)
        for (dirpath, dirnames, filenames) in self.f:
            for filename in filenames:
                self.dirdict[str(filename).split(".")[0]] = os.path.join(dirpath, filename)

    '''写入yaml文件'''
    def Wyaml(self,content,K):
        with open(self.dirdict[K],'w',encoding='utf-8') as f:
            yaml.dump(content,f)

    '''读取yaml文件'''
    def Rallyaml(self,K):
        with open(self.dirdict[K],'r',encoding='utf-8') as f:
            return yaml.load(f)

    def path_log(self):
        with open(self.app,'r',encoding='utf-8') as f:
            p2=yaml.load(f)['path_log']
            path = os.path.join(self.path2, p2)
            return path
if __name__ == '__main__':
    print(os.listdir(os.path.dirname(os.path.abspath('.')) + "\\test_data"))
    pa = {}
    f = os.walk(os.path.dirname(os.path.abspath('.')) + "\\test_data",topdown=True,onerror=None,followlinks=False)
    for (dirpath,dirnames,filenames) in f:
        for filename in filenames:
            pa[str(filename).split(".")[0]] = os.path.join(dirpath,filename)

    print(pa)