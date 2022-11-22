import datetime
import time

import pymysql


class Query:
    def __init__(self):
        HOST = 'localhost'  # 主机名
        USER = 'root'  # 用户名
        PASSWORD = '3981786cc'  # 密码
        DB = 'work_db'  # 数据库名称
        PORT = 3306  # 端口号
        CHARSET = 'utf8'  # 字符集类型
        try:
            self.conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
        except BaseException:
            print("Error: 数据库链接失败")

    # 查找XX表的数据
    def search_db(self, db_name, x):
        sql = "SELECT * FROM " + db_name + " WHERE id = %s"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(sql, x)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results[0]

    def fetch(self, dayTime):
        sql = "SELECT * FROM ads_task WHERE dayTime = %s "
        na = dayTime
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, na)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except BaseException:
            print("Error: 没有找到数据")

    def add(self, taskName, value, acd):
        dayTime = time.strftime('%Y-%m-%d')
        nowTime = time.strftime('%H:%M:%S')
        selectSql = "SELECT * FROM ads_task WHERE id = '" + acd + "' and dayTime = '" + dayTime + "'"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(selectSql)
        # 获取所有记录列表
        results = cursor.fetchall()

        if len(results) > 0:
            sql = "update ads_task set " + taskName + "=%s ,runTime = %s  where  id = %s and dayTime = %s"
            val = (value, nowTime, acd, dayTime)
            cursor.execute(sql, val)
            self.conn.commit()
            self.conn.close()
        else:
            sql = 'INSERT INTO ads_task (id, dayTime, runTime,' + taskName + ') VALUES (%s,%s,%s,%s)'
            val = (acd, dayTime, nowTime, value)
            cursor.execute(sql, val)
            self.conn.commit()
            self.conn.close()

    def delete(self):
        dayTime = datetime.datetime.today().date()
        lastTime = dayTime - datetime.timedelta(days=2)
        sql = "DELETE FROM ads_task WHERE dayTime <= %s"
        val = lastTime
        cursor = self.conn.cursor()
        cursor.execute(sql, val)
        self.conn.commit()
        self.conn.close()

    def close(self):
        self.conn.close()
