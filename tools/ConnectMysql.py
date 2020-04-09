import pymysql
import datetime

# from Log import *
# 打开数据库连接
class ConnectMysql():
    def __init__(self):
        self.nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.con = Config().get_db()["bms"]
        self.db = pymysql.connect(self.con["host"], self.con["user"], self.con["password"], self.con["db"])

    def update_mysql(self, mysql):
        '''设置成教学员附件资料'''
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        # SQL 更新语句
        try:
            cursor.execute(mysql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def insert_into_mysql(self, mysql):
        '''设置成教学员附件资料'''
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        try:
            cursor.execute(mysql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def select_mysql(self, mysql):
        '''获取学员std_id'''
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        try:
            cursor.execute(mysql)
            # 使用 fetchone() 方法获取元组单条数据.
            # data = cursor.fetchone()
            data = cursor.fetchall()
            return data
        except:
            self.db.rollback()
            print('你的sql写错了！！！！')
        self.db.close()


if __name__ == '__main__':
    mysql2 = "SELECT out_id FROM bms.bd_student_out WHERE std_id = '155969367842945105'"
    annex_id = ConnectMysql().select_mysql(mysql2)
    print(annex_id[0][0])
