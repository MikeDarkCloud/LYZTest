'''
配置文件--配置公共参数
'''
import os
import yaml

class Config:
    def __init__(self):
        self.dirdict={}
        self.path1 = os.getcwd()     #正式用
        self.path2 = os.path.dirname(os.path.abspath('.'))  #调试用
        self.app = self.path1 + "\\config\\application.yaml"
        # self.f = os.walk(os.path.dirname(os.path.abspath('.')) + "\\test_data", topdown=True, onerror=None, followlinks=False)
        # self.f = os.walk(os.getcwd() + "\\test_data", topdown=True, onerror=None, followlinks=False)
        self.f = os.walk(self.path1 + "\\test_data", topdown=True, onerror=None, followlinks=False)
        for (dirpath, dirnames, filenames) in self.f:
            for filename in filenames:
                self.dirdict[str(filename).split(".")[0]] = os.path.join(dirpath, filename)

    '''写入yaml文件'''
    def Wyaml(self,content,YamlFile):
        with open(self.dirdict[YamlFile],'w',encoding='utf-8') as f:
            yaml.dump(content,f,default_flow_style=False,encoding='utf-8',allow_unicode=True)

    '''读取yaml文件'''
    def Rallyaml(self,K):
        with open(self.dirdict[K],'r',encoding='utf-8') as f:
            return yaml.load(f)

    def getPath(self,K):
        with open(self.app,'r',encoding='utf-8') as f:
            p2=yaml.load(f)[K]
            path = os.path.join(self.path1, p2)
            return path

    def getApplication(self,K):
        with open(self.app,'r',encoding='utf-8') as f:
            p2=yaml.load(f)[K]
            return p2

if __name__ == '__main__':
    '''调试'''
    print(os.listdir(os.path.dirname(os.path.abspath('.')) + "\\test_data"))
    pa = {}
    f = os.walk(os.path.dirname(os.path.abspath('.')) + "\\test_data",topdown=True,onerror=None,followlinks=False)
    for (dirpath,dirnames,filenames) in f:
        for filename in filenames:
            pa[str(filename).split(".")[0]] = os.path.join(dirpath,filename)

    print(pa)