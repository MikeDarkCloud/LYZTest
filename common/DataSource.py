from common.conf import *
from tools.CreateIdentity import *
from tools.CreateMobile import *
class DataSource():
    def __init__(self):
        self.f = Config()


    def getBaseUrl(self):
        '''获取测试环境地址'''
        return self.f.getApplication('baseUrl')

    def getLogPath(self):
        '''获取配置的日志存储路径'''
        return self.f.getApplication('logPath')

    def getHearder(self,type = None):
        '''获取消息头'''
        if type == None:
            return self.f.Rallyaml('Hearder').get('Hearders0')

        if type == 'login' or type == 'Login':
            return self.f.Rallyaml('Hearder').get('LHearders')

        if type == 'regiester':
            return self.f.Rallyaml('Hearder').get('RHearders')

    def setHearder(self,V):
        H=self.f.Rallyaml('Hearder')
        H['RHearders']['Content-Type']=V
        self.f.Wyaml(H, 'Hearder')


    def setCookie(self,value):
        '''获取cookie'''
        load = self.f.Rallyaml('Logining')
        load['Cookie'] = value
        self.f.Wyaml(load,'Logining')

    def setYaml(self,Rallyaml,fname,):
        '''x写入内容到Yaml'''
        self.f.Wyaml(Rallyaml,fname)


    def getCookie(self):
        '''获取cookies'''
        return self.f.Rallyaml('Logining').get('Cookie')


    def getRallyaml(self,Yaml):
        '''获取文件实例'''
        return self.f.Rallyaml(Yaml)


    def getIdcard(self):
        '''随机获取身份证'''
        return create_identity(int(area_dict1), random.randint(18, 30), random.randint(1, 2))


    def getMobile(self):
        '''获取手机号'''
        return get_mobile()

    def setLearnInfo(self,key0,key1,value):
        '''保存学员信息'''
        Rallyaml=self.getRallyaml('LearnInfo')
        Rallyaml[key0][key1]=value
        self.setYaml(Rallyaml,'LearnInfo')

    def getLearnInfo(self,key0,key1):
        '''获取学员信息'''
        return self.getRallyaml('LearnInfo')[key0][key1]


if __name__ == '__main__':
    # print(DataSource().getHearders())
    # print(DataSource().getHearders('login'))
    # print(DataSource().getHearders('regiester'))
    DataSource().setCookie('666666')
    print(DataSource().getCookie())