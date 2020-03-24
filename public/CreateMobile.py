import random
from pubilc.ConnectMysql import *
'''生成随机号码'''
def get_mobile():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
                "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def create_mobile():
    mobile = get_mobile()
    istrue = ConnectMysql().select_mysql("SELECT count(*) FROM bms.bd_learn_info WHERE mobile = '%s'" %mobile)
    if (istrue[0][0]  != 0):
        return create_mobile()
    else:
        return mobile

if __name__ == '__main__':
    print(create_mobile())