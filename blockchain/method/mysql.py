import datetime
import time

import pymysql


class Mysql:
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

    # 新建数据_ads
    def creartDb_ads(self):
        today = datetime.date.today()
        # 新建id=1到50且daytime=当天日期的记录
        for i in range(1, 51):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM ads_task WHERE id = %s AND daytime = %s", (i, today))
            result = cursor.fetchone()

            if not result:
                cursor.execute("INSERT INTO ads_task (id, daytime) VALUES (%s, %s)", (i, today))
                self.conn.commit()

    # 新建数据_bit
    def creartDb_bit(self):
        today = datetime.date.today()
        # 新建id=1到100且daytime=当天日期的记录
        for i in range(1, 101):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM bit_task WHERE id = %s AND daytime = %s", (i, today))
            result = cursor.fetchone()

            if not result:
                cursor.execute("INSERT INTO bit_task (id, daytime) VALUES (%s, %s)", (i, today))
                self.conn.commit()

    # 查找XX表的数据
    def search_db(self, db_name, x):
        sql = "SELECT * FROM " + db_name + " WHERE id = %s"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(sql, x)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results[0]

    def add_wallet(self, tableName, taskName, value, x):
        sql = "SELECT * FROM " + tableName + " WHERE id = %s"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(sql, x)
        # 获取所有记录列表
        results = cursor.fetchall()
        sql = "update " + tableName + " set " + taskName + "=%s  where  id = %s"
        val = (value, x)
        cursor.execute(sql, val)
        self.conn.commit()

    # 查找数据（2个条件）
    def findDate(self, tableName, taskName, value):
        dayTime = time.strftime('%Y-%m-%d')
        sql = "SELECT * FROM " + tableName + " WHERE dayTime = '" + dayTime + "' AND (" + taskName + " LIKE '%" + value + "%' OR " + taskName + " IS NULL)"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            result_list = [row[0] for row in results]
            return result_list
        except BaseException:
            print("Error: 没有找到数据")

    # 查找数据（3个条件）
    def findDate_3(self, tableName, taskName, value1, value2):
        dayTime = time.strftime('%Y-%m-%d')
        sql = "SELECT * FROM " + tableName + " WHERE dayTime = '" + dayTime + "' AND (" + taskName + " LIKE '%" + value1 + "%' OR " + taskName + " LIKE '%" + value2 + "%' OR " + taskName + " IS NULL)"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            result_list = [row[0] for row in results]
            return result_list
        except BaseException:
            print("Error: 没有找到数据")

    # 查找数据（2个条件，不包含某个字符）
    def findDate_No(self, tableName, taskName, value):
        dayTime = time.strftime('%Y-%m-%d')
        sql = "SELECT * FROM " + tableName + " WHERE dayTime = '" + dayTime + "' AND (" + taskName + " NOT LIKE '%" + value + "%' OR " + taskName + " IS NULL)"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            result_list = [row[0] for row in results]
            return result_list
        except BaseException:
            print("Error: 没有找到数据")

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

    # 统计数据库总行数
    def all_db(self, db_name):
        sql = "SELECT * FROM " + db_name
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def add(self, tableName, taskName, value, acd):
        dayTime = time.strftime('%Y-%m-%d')
        nowTime = time.strftime('%H:%M:%S')
        selectSql = "SELECT * FROM " + tableName + " WHERE id = '" + acd + "' and dayTime = '" + dayTime + "'"
        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()
        cursor.execute(selectSql)
        # 获取所有记录列表
        results = cursor.fetchall()

        if len(results) > 0:
            sql = "update " + tableName + " set " + taskName + "=%s ,runTime = %s  where  id = %s and dayTime = %s"
            val = (value, nowTime, acd, dayTime)
            cursor.execute(sql, val)
            self.conn.commit()
        else:
            sql = 'INSERT INTO ' + tableName + ' (id, dayTime, runTime,' + taskName + ') VALUES (%s,%s,%s,%s)'
            val = (acd, dayTime, nowTime, value)
            cursor.execute(sql, val)
            self.conn.commit()

    def delete(self, tableName):
        dayTime = datetime.datetime.today().date()
        lastTime = dayTime - datetime.timedelta(days=2)
        sql = "DELETE FROM " + tableName + " WHERE dayTime <= %s"
        val = lastTime
        cursor = self.conn.cursor()
        cursor.execute(sql, val)
        self.conn.commit()

    def close(self):
        self.conn.close()
