"""
@author:lanmingyong
@time:20200429
"""
from locust.clients import HttpSession
from locust import *
from common.DataSource import DataSource
from public.TestCaseAssembly import TestCaseAssembly, BeforeParamCom
from public.AfterParamCom import *
from requests_toolbelt import MultipartEncoder
import queue


class LoadLocust(TaskSequence):

    @seq_task(1)
    def test_00_login(self):
        t = DataSource().getAllyaml('Logining')
        url = str(t.get('urls'))
        data = dict(t.get('data'))
        try:
            data['mobile'] = self.locust.queueData.get()
            print(data)
        except queue.Empty:
            print('no data exit')
            exit(0)
        headers = {
            "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
            "Host": 'bms-3.yzwill.cn',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = self.client.post(url=url, data=data, headers=headers, verify=False)
        print(response.text)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")

    @seq_task(2)
    def test_0_getGkOpenEnrollCityInfo(self):
        '''随机获取国开报读城市'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('getGkOpenEnrollCityInfo', (intFile.getYamlParms(('GK', 'grade'), ), intFile.getYamlParms(('GK', 'level'))),
                                              (('data', 'ext2'), ('data', 'ext1')))

        headers = {
            "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
            "Host": 'bms-3.yzwill.cn',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = self.client.post(url=case[2], data=case[3], headers=headers, verify=False)
        print(response.text)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")

    @seq_task(3)
    def test_1_sUnvs(self):
        '''随机获取国开院校ID'''
        intFile = YamlParser('StudentInfo')
        case = TestCaseAssembly().setAipParam('sUnvs', (intFile.getYamlParms(('GK', 'recruitType')),), ('data', 'ext1'))
        headers = {
            "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
            "Host": 'bms-3.yzwill.cn',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = self.client.post(url=case[2], data=case[3], headers=headers, verify=False)
        print(response.text)
        if response.status_code == 200:
            print("success")
        else:
            print("fails")




class WebsiteUser(HttpLocust):
    mobilList = [13560148201, 13726716401,13300010001,13526323252,13168552424,16655441122]
    task_set = LoadLocust
    host = "http://bms-3.yzwill.cn"
    queueData = queue.Queue()
    for i in mobilList:
        queueData.put(i)
    min_wait = 3000
    max_wait = 6000
