from common.conf import *
class YamlParser():
    def __init__(self,YFile):
        self.Ya = YFile
        self.Yaml = Config().Rallyaml(YFile)   #LearnInfo

    def getYamlParms(self,tupe:tuple):
        if len(tupe) == 0 or len(tupe)>=6:
            raise Exception("参数不能为空或参数超过5个！")
        if len(tupe) == 1:
            return self.Yaml.get(tupe[0])

        if len(tupe) == 2:
            return self.Yaml[tupe[0]][tupe[1]]

        if len(tupe) == 3:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]]

        if len(tupe) == 4:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]]

        if len(tupe) == 5:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]][tupe[4]]

    def setYaml(self,value,Key:tuple):
        K = 0
        if isinstance(Key, str):  # ('aa','bb')
            self.Yaml[Key] = value
            Config().Wyaml(self.Yaml, self.Ya)
        if  len(Key)>=2:
            if isinstance(Key[0], tuple):  # (('aa','bb','cc'),('dd','ee','ff'),('jj','hh','ii'))
                for i in Key:
                    # 取出一个d[0][0]('aa','bb','cc')
                    if isinstance(Key[K], tuple):  # ('aa','bb','cc')
                        if len(Key[K]) == 1:
                            self.Yaml[Key[K][0]] = value[K]
                            Config().Wyaml(self.Yaml,self.Ya)

                        if len(Key[K]) == 2:
                            self.Yaml[Key[K][0]][Key[K][1]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Key[K]) == 3:
                            self.Yaml[Key[K][0]][Key[K][1]] [Key[K][2]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Key[K]) == 4:
                            self.Yaml[Key[K][0]][Key[K][1]][Key[K][2]][Key[K][3]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)

                        if len(Key[K]) == 5:
                            self.Yaml[Key[K][0]][Key[K][1]][Key[K][2]][Key[K][3]][Key[K][4]] = value[K]
                            Config().Wyaml(self.Yaml, self.Ya)
                    K = K + 1
        if  len(Key)==1:
            if isinstance(Key[0], tuple):  # ('aa','bb','cc')
                if len(Key[0]) == 1:
                    i = len(Key[0])
                    self.Yaml[Key[0][0]] = value
                    Config().Wyaml(self.Yaml,self.Ya)
                if len(Key[0]) == 2:
                    k = len(Key[0])
                    self.Yaml[Key[0][0]][Key[0][1]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Key[0]) == 3:
                    self.Yaml[Key[0][0]][Key[0][1]][Key[0][2]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Key[0]) == 4:
                    self.Yaml[Key[0][0]][Key[0][1]][Key[0][2]][Key[0][3]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
                if len(Key[0]) == 5:
                    self.Yaml[Key[K][0][0]][Key[0][1]][Key[0][2]][Key[0][3]][Key[0][4]] = value
                    Config().Wyaml(self.Yaml, self.Ya)
    def saveYaml(self,dictV):
        Config().Wyaml(dictV,self.Ya)
