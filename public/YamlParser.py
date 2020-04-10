from common.conf import *
class YamlParser():
    def __init__(self,YFile):
        self.Ya = YFile
        self.con = Config()
        self.Yaml = self.con.Rallyaml(self.Ya)

    def getYamlParms(self,*kwargs):
        if len(kwargs) == 0 or len(kwargs)>=6:
            raise Exception("参数不能为空或参数超过5个！")
        if len(kwargs) == 1:
            self.Yaml.keys()
            return self.Yaml.get(kwargs[0])

        if len(kwargs) == 2:
            return self.Yaml[kwargs[0]][kwargs[1]]

        if len(kwargs) == 3:
            return self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]]

        if len(kwargs) == 4:
            return self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]][kwargs[3]]

        if len(kwargs) == 5:
            return self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]][kwargs[3]][kwargs[4]]

    def setYaml(self,value,*kwargs):
        if len(kwargs) == 0 or len(kwargs)>=6:
            raise Exception("参数不能为空或参数超过5个！")
        if len(kwargs) == 1:
            self.Yaml[kwargs[0]] = value
            self.con.Wyaml(self.Yaml,self.Ya)

        if len(kwargs) == 2:
            self.Yaml[kwargs[0]][kwargs[1]] = value
            self.con.Wyaml(self.Yaml, self.Ya)

        if len(kwargs) == 3:
            self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]]= value
            self.con.Wyaml(self.Yaml, self.Ya)
        if len(kwargs) == 4:
            self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]][kwargs[3]]= value
            self.con.Wyaml(self.Yaml, self.Ya)
        if len(kwargs) == 5:
            self.Yaml[kwargs[0]][kwargs[1]][kwargs[2]][kwargs[3]][kwargs[4]]= value
            self.con.Wyaml(self.Yaml, self.Ya)