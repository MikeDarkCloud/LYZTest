"""
@author:lanmingyong
@time:20200429
"""
from common.DataSource import DataSource
from locust import *

class LoadLocust(TaskSet):

    @task
    def test_00_login(self):
        t= DataSource().getAllyaml('Logining')
        url = str(t.get('urls'))
        data = dict(t.get('data'))
        headers = {
      "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
      "Host": 'bms-3.yzwill.cn',
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/73.0.3683.86 Safari/537.36"
      }
        req = self.client.post(url=url,data=data, headers=headers,verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")


class WebsiteUser(HttpLocust):
    task_set = LoadLocust
    host = "http://bms.yzwill.cn"
    min_wait = 1000
    max_wait = 5000


