from common.conf import *
class YamlParser():
    def __init__(self,YFile):
        self.Ya = YFile
        self.con = Config()
        self.Yaml = Config().Rallyaml(YFile)



    def getYamlParms(self,tupe):
        if len(tupe) == 0 or len(tupe)>=6:
            raise Exception("参数不能为空或参数超过5个！")
        if len(tupe) == 1:
            self.Yaml.keys()
            return self.Yaml.get(tupe[0])

        if len(tupe) == 2:
            ee='GK'
            Eee=tupe
            twt=self.Yaml.get(ee)
            ttt=self.Yaml.get(Eee)
            tr=self.Yaml[str(tupe[0])][str(tupe[1])]
            return self.Yaml[str(tupe[0])][str(tupe[1])]

        if len(tupe) == 3:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]]

        if len(tupe) == 4:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]]

        if len(tupe) == 5:
            return self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]][tupe[4]]

    def setYaml(self,value,tupe):
        if len(tupe) == 0 or len(tupe)>=6:
            raise Exception("参数不能为0个或参数超过5个！")

        if len(tupe) == 1:
            self.Yaml[tupe[0]] = value
            self.con.Wyaml(self.Yaml,self.Ya)

        if len(tupe) == 2:
            self.Yaml[tupe[0]][tupe[1]] = value
            self.con.Wyaml(self.Yaml, self.Ya)

        if len(tupe) == 3:
            self.Yaml[tupe[0]][tupe[1]][tupe[2]]= value
            self.con.Wyaml(self.Yaml, self.Ya)
        if len(tupe) == 4:
            self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]]= value
            self.con.Wyaml(self.Yaml, self.Ya)
        if len(tupe) == 5:
            self.Yaml[tupe[0]][tupe[1]][tupe[2]][tupe[3]][tupe[4]]= value
            self.con.Wyaml(self.Yaml, self.Ya)

    def addValues(self):
        pass