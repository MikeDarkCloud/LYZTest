# -*-coding:utf-8-*-
'''
配置文件--配置公共参数
'''
import os
import yaml


class Config():
    def __init__(self):
        self.path1 = os.getcwd()
        self.path2 = os.path.dirname(os.path.abspath('.'))
        # self.path2 = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
        file_path = self.path2 + "\\conf\\conf.yml"
        file = open(str(file_path), encoding='utf-8')
        self.data = yaml.load(file)

    def url(self):
        url = self.data["bms"]
        return url

    def urls(self):
        urls = self.data["zm"]
        return urls

    def path_log(self):
        # p1 = self.path2
        p2 = self.data["path_log"]
        path = os.path.join(self.path2, p2)
        return path

    def path_xlexcel(self):
        p1 = self.path2
        p2 = self.data["path_excel"]
        # 调试用
        # path = os.path.join(p1, p2)
        # 正式用
        path = os.path.join(self.path2, p2)
        return path

    def path_case(self):
        p2 = self.data["path_case"]
        path = os.path.join(self.path2, p2)
        return path

    def path_report(self):
        p1 = self.path2
        p2 = self.data["path_report"]
        path = os.path.join(self.path2, p2)
        return path

    def path_jpg(self):
        p1 = self.path2
        p2 = self.data["path_jpg"]
        # 调试用
        # path = os.path.join(p1, p2)
        # 正式用
        path = os.path.join(self.path2, p2)
        return path

    def get_Invitation_url(self):
        '''邀约链接'''
        url = "http://zm-3.yzwill.cn/invite?action=login&inviteId=74c%2BQfTz20Ckbk8BiyTPt%2BrrtJMpWANS"
        return url

    def loginUser(self):
        username = self.data["bmslogin"]["username"]
        password = self.data["bmslogin"]["password"]
        return username, password

    def getEmailSender(self):
        sender = self.data["send"]["sender"]
        pwd = self.data["send"]["pwd"]

        return sender, pwd

    def getEmailReceiver(self):
        receiver = self.data["receiver"]
        return receiver

    def get_db(self):
        db = self.data["db"]
        return db


if __name__ == '__main__':
    # print(Config().path_case())
    # print(Config().path_jpg())
    # print(Config().path_log())
    # print(Config().path_report())
    # print(Config().path_xlexcel())
    print(Config().get_db()["bms"])
