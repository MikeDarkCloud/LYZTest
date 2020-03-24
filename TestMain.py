import BSTestRunner
import unittest
import time
from email.header import Header
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from Config import *

'''
# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）

'''


def add_case(case_path, rule):
    '''加载所有的测试用例'''
    testunit = unittest.TestSuite()

    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    # discover = unittest.defaultTestLoader.discover(case_path,pattern="test_login.py")
    # discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         testunit.addTests(test_case)
    #         print(testunit)
    # return testunit.addTests(discover)

    testunit.addTests(discover)
    # # 直接加载discover
    # print(testunit)
    return testunit


def run_case(all_case, report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_spath = os.path.join(report_path, now + "result.html")
    fp = open(report_spath, "wb")
    runner = BSTestRunner.BSTestRunner(stream=fp,
                                       title='远智教务系统接口自动化测试报告：',
                                       description='用例执行情况：')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print('最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file):
    '''发送最新的测试报告内容'''
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
        # 定义邮件内容
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg["Subject"] = Header("自动化测试报告", 'utf-8').encode()
        msg["From"] = "lanmingyong"
        # msg["From"] = sender
        msg["To"] = '975922642@qq.com'
        # msg["To"] = receiver
        # 加上时间戳
        msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
        msg.attach(body)
        # 添加附件
        # att = MIMEText(open(report_file, "rb").read(), "plain", "utf-8")
        att = MIMEText(open(report_file, "rb").read(), "html", "utf-8")
        # att = MIMEText(open(report_file, "rb").read(), "html", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)

        # 登录邮箱
        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(smtpserver, '25')
        # 用户名密码
        smtp.login(sender, psw)

        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')


if __name__ == "__main__":
    # 测试用例的路径、匹配规则
    case_path = Config().path_case()
    rule = "test*.py"
    all_case = add_case(case_path, rule)  # 1加载用例
    # 生成测试报告的路径
    report_path = Config().path_report()
    run_case(all_case, report_path)  # 2执行用例
    # 获取最新的测试报告文件
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # 邮箱配置
    # sender = "mike"
    # sender = "975922642@qq.com"
    sender = 'lanmingyong@126.com'
    psw = 'mike5788973'
    # psw = "zlongcnkoqlwdajj"
    # 收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com',
    receiver = "lanmy@yzou.cn,975922642@qq.com"
    # receiver = "lanmingyong@126.com"
    smtp_server = 'smtp.126.com'
    # smtp_server = 'smtp.qq.com'
    send_mail(sender, psw, receiver, smtp_server, report_file)
    # 4最后一步发送报告，需要发邮件就取消注释
