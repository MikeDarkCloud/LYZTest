'''
@description:YAML文件核心解析器
@author:lanmingyong
'''
from common.conf import *
class YamlParser():
    def __init__(self,YFile):
        self.Ya = YFile
        self.Yaml = Config().Rallyaml(YFile)

    def getYamlParms(self, keys:tuple):
        if len(keys) == 0 or len(keys)>=6:
            raise Exception("参数不能为空或参数超过5个！")
        if len(keys) == 1:
            return self.Yaml.get(keys[0])

        if len(keys) == 2:
            return self.Yaml[keys[0]][keys[1]]

        if len(keys) == 3:
            return self.Yaml[keys[0]][keys[1]][keys[2]]

        if len(keys) == 4:
            return self.Yaml[keys[0]][keys[1]][keys[2]][keys[3]]

        if len(keys) == 5:
            return self.Yaml[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]

    def setYaml(self, value, Keys:tuple):
        K = 0
        if isinstance(Keys, str):
            self.Yaml[Keys] = value
            Config().Wyaml(self.Yaml, self.Ya)
        if  len(Keys)>=2:
            if isinstance(Keys[0], tuple):
                for i in Keys:
                    if isinstance(Keys[K], tuple):
                        if len(Keys[K]) == 1:
                            self.Yaml[Keys[K][0]] = value[K]
                            Config().Wyaml(self.Yaml,self.Ya)

                        if len(Keys[K]) == 2:
                            self.Yaml[Keys[K][0]][Keys[K][1]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Keys[K]) == 3:
                            self.Yaml[Keys[K][0]][Keys[K][1]] [Keys[K][2]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Keys[K]) == 4:
                            self.Yaml[Keys[K][0]][Keys[K][1]][Keys[K][2]][Keys[K][3]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Keys[K]) == 5:
                            self.Yaml[Keys[K][0]][Keys[K][1]][Keys[K][2]][Keys[K][3]][Keys[K][4]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)
                    K = K + 1
        if  len(Keys)==1:
            if isinstance(Keys[0], tuple):
                if len(Keys[0]) == 1:
                    self.Yaml[Keys[0][0]] = value
                    Config().Wyaml(self.Yaml,self.Ya)
                if len(Keys[0]) == 2:
                    self.Yaml[Keys[0][0]][Keys[0][1]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Keys[0]) == 3:
                    self.Yaml[Keys[0][0]][Keys[0][1]][Keys[0][2]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Keys[0]) == 4:
                    self.Yaml[Keys[0][0]][Keys[0][1]][Keys[0][2]][Keys[0][3]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Keys[0]) == 5:
                    self.Yaml[Keys[K][0][0]][Keys[0][1]][Keys[0][2]][Keys[0][3]][Keys[0][4]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
    def saveYaml(self,dictV):
        Config().Wyaml(dictV,self.Ya)
