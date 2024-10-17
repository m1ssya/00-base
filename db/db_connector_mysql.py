import mysql.connector
from mysql.connector import Error
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MySQLConnector:
    """
    MySQL数据库连接器类,用于管理数据库连接和执行SQL查询。
    """

    def __init__(self, host, user, password, database):
        """
        初始化MySQLConnector实例。

        参数:
        host (str): MySQL服务器主机地址
        user (str): 数据库用户名
        password (str): 数据库密码
        database (str): 要连接的数据库名称
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        logger.info(f"初始化MySQLConnector: host={host}, user={user}, database={database}")

    def connect(self):
        """
        建立与MySQL数据库的连接。

        如果连接成功,会创建一个数据库游标。
        如果连接失败,会记录错误信息。
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logger.info(f"成功连接到MySQL数据库: {self.host}/{self.database}")
                self.cursor = self.connection.cursor()
        except Error as e:
            logger.error(f"连接MySQL数据库失败: {self.host}/{self.database}. 错误: {e}")

    def disconnect(self):
        """
        关闭与MySQL数据库的连接。

        如果存在活动连接,会关闭游标和连接。
        """
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            logger.info(f"已断开与MySQL数据库的连接: {self.host}/{self.database}")

    def __del__(self):
        """
        析构函数，在对象被销毁时调用。
        确保在对象被销毁时断开数据库连接。
        """
        self.disconnect()
        logger.info(f"数据库连接已断开: {self.host}/{self.database}")

    def execute_query(self, query, params=None):
        """
        执行SQL查询,不返回结果。

        适用于INSERT, UPDATE, DELETE等操作。

        参数:
        query (str): 要执行的SQL查询语句
        params (tuple, optional): 查询参数,用于参数化查询

        如果执行成功,会自动提交更改。
        如果执行失败,会记录错误信息。
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            logger.info("查询执行成功")
        except Error as e:
            logger.error(f"执行查询时出错: {e}")

    def fetch_all(self, query, params=None):
        """
        执行SELECT查询并返回所有结果。

        参数:
        query (str): 要执行的SELECT查询语句
        params (tuple, optional): 查询参数,用于参数化查询

        返回:
        list of tuples: 查询结果的所有行
        None: 如果查询执行出错
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            logger.error(f"获取数据时出错: {e}")
            return None

    def fetch_one(self, query, params=None):
        """
        执行SELECT查询并返回单个结果。

        参数:
        query (str): 要执行的SELECT查询语句
        params (tuple, optional): 查询参数,用于参数化查询

        返回:
        tuple: 查询结果的第一行
        None: 如果查询执行出错或没有结果
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except Error as e:
            logger.error(f"获取数据时出错: {e}")
            return None


if __name__ == "__main__":
    # 使用示例
    db = MySQLConnector(host="localhost", user="your_username", password="your_password", database="your_database")

    try:
        # 连接到数据库
        db.connect()

        # 执行INSERT操作
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        db.execute_query(insert_query, ("张三", "zhangsan@example.com"))

        # 执行SELECT操作并获取所有结果
        select_all_query = "SELECT * FROM users"
        results = db.fetch_all(select_all_query)
        if results:
            logger.info("所有用户:")
            for row in results:
                logger.info(row)

        # 执行SELECT操作并获取单个结果
        select_one_query = "SELECT * FROM users WHERE name = %s"
        result = db.fetch_one(select_one_query, ("张三",))
        if result:
            logger.info("查找到的用户:")
            logger.info(result)

    except Exception as e:
        logger.error(f"操作过程中出现错误: {e}")

    finally:
        # 确保在结束时断开连接
        db.disconnect()
