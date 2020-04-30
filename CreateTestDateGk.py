from common.DataSource import DataSource
from common.Log import Log
from common.base import YzApi
from public.TestCaseAssembly import TestCaseAssembly, BeforeParamCom
from public.AfterParamCom import *
from requests_toolbelt import MultipartEncoder

from public.TestCaseAssert import MyAssert
import sys

class MyTestCase():
    def __init__(self):
        self.log = Log()
        self.test_00_login()

    def test_00_login(self):
        YzApi().login()


    def test_0_getGkOpenEnrollCityInfo(self):
        '''随机获取国开报读城市'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('getGkOpenEnrollCityInfo', (intFile.getYamlParms(('GK', 'grade'),), intFile.getYamlParms(('GK', 'level'))),
                                              (('data', 'ext2'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getGkOpenEnrollCityInfo', ('GStudent', 'city'))

    # @unittest.skip("skipping")
    def test_1_sUnvs(self):
        '''随机获取国开院校ID'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('sUnvs', (intFile.getYamlParms(('GK', 'recruitType')),), ('data', 'ext1'))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'sUnvs', ('GStudent', 'unvsId'))

    # @unittest.skip("skipping")
    def test_2_getOpenTestAreaByCity(self):
        '''随机获取国开报读考区ID+考区名称'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenTestAreaByCity', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'city'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getOpenTestAreaByCity', (('GStudent', 'taId'), ('GStudent', 'taName')))

    # @unittest.skip("skipping")
    def test_3_getOpenPfsnByTaId(self):
        '''随机获取国开报读专业pfsnId+专业名称pfsnName+专业编号pfsnCode'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('getOpenPfsnByTaId', (
        intFile.getYamlParms(('GK', 'level')), intFile.getYamlParms(('GK', 'grade')), extFile.getYamlParms(('GStudent', 'taId'))),
                                              (('data', 'ext2'), ('data', 'ext3'), ('data', 'ext1')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数'''
        AfterParamCom().saveParam(response.text, 'getOpenPfsnByTaId', (('GStudent', 'pfsnId'), ('GStudent', 'pfsnName'), ('GStudent', 'pfsnCode')))

    def test_4_showFeeList(self):
        '''获取国开报读收费标准信息'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        case = TestCaseAssembly().setAipParam('showFeeList', (
        intFile.getYamlParms(('GK', 'recruitType')), intFile.getYamlParms(('GK', 'scholarships')), extFile.getYamlParms(('GStudent', 'pfsnId')),
        extFile.getYamlParms(('GStudent', 'taId'))), (('data', 'recruitType'), ('data', 'scholarship'), ('data', 'pfsnId'), ('data', 'taId')))
        response = YzApi().lapi(method=case[0], headers=case[1], urls=case[2], data=case[3])
        '''提取参数'''
        AfterParamCom().saveJson(response.text, (('body', 'feeInfo', 'feeId'),), (('GStudent', 'feeId'),))
        AfterParamCom().saveParam(response.text, 'showFeeList', ('GStudent', 'feeList'))

    # @unittest.skip("skipping")
    def test_5_gk_normal_register(self):
        '''随机录入国开类型学员学员'''
        intFile = YamlParser('StudentInfo')
        extFile = YamlParser('LearnInfo')
        '''从配置文件获取参数'''
        grade = intFile.getYamlParms(('GK', 'grade'))
        recruitType = intFile.getYamlParms(('GK', 'recruitType'))
        scholarship = intFile.getYamlParms(('GK', 'scholarships'))
        '''从参数文件获取参数'''
        city = extFile.getYamlParms(('GStudent', 'city'))
        unvsId = extFile.getYamlParms(('GStudent', 'unvsId'))
        feeId = extFile.getYamlParms(('GStudent', 'feeId'))
        feeList = extFile.getYamlParms(('GStudent', 'feeList'))
        pfsnCode = extFile.getYamlParms(('GStudent', 'pfsnCode'))
        pfsnId = extFile.getYamlParms(('GStudent', 'pfsnId'))
        pfsnName = extFile.getYamlParms(('GStudent', 'pfsnName'))
        taId = extFile.getYamlParms(('GStudent', 'taId'))
        taName = extFile.getYamlParms(('GStudent', 'taName'))
        mobile =BeforeParamCom().getPhone()
        idCard =BeforeParamCom().getCard()
        self.log.info('学员手机号：'+mobile)
        self.log.info('学员身份证号：'+str(idCard))
        BeforeParamCom().setLearn((('GStudent', 'mobile'),), mobile)
        BeforeParamCom().setLearn((('GStudent', 'idCard'),), idCard)

        pfsnLevel = intFile.getYamlParms(('GK', 'pfsnLevel'))

        '''将参数组合到接口文件'''
        values = (str(grade),str(recruitType),str(scholarship),str(city),str(unvsId),str(feeList),str(pfsnCode),
                  str(pfsnId),str(pfsnName),str(taId),str(taName),mobile,idCard,str(pfsnLevel),str(feeId))
        keys = (('data', 'grade'),('data', 'recruitType'),('data', 'scholarship'),('data', 'city'),('data', 'unvsId'),
                ('data', 'feeList'), ('data', 'pfsnCode'), ('data', 'pfsnId'), ('data', 'pfsnName'), ('data', 'taId'),
                ('data', 'taName'),('data', 'mobile'),('data', 'idCard'),('data', 'pfsnLevel'),('data', 'feeId'))
        case = TestCaseAssembly().setAipParam('GrecruitAdd',values,keys,'regiester')
        data = MultipartEncoder(fields=case[3])
        DataSource().setHearder(data.content_type)
        response = YzApi().lapi(method=case[0], headers=DataSource().getHearder("regiester"), urls=case[2],data=data)



    def testing(self):
        self.test_0_getGkOpenEnrollCityInfo()
        self.test_1_sUnvs()
        self.test_2_getOpenTestAreaByCity()
        self.test_3_getOpenPfsnByTaId()
        self.test_4_showFeeList()
        self.test_5_gk_normal_register()


    def testing1(self):
        self.test_5_gk_normal_register()

    def testing2(self):
        self.test_0_getGkOpenEnrollCityInfo()
        self.test_2_getOpenTestAreaByCity()
        self.test_4_showFeeList()
        self.test_5_gk_normal_register()

if __name__ == '__main__':
    i = 1
    t=MyTestCase()
    while i > 0:
        t.testing()
        # t.testing2()
        i -= 1





