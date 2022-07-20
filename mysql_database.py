# Developer : Lucas Liu
# Date: 6/10/2022 Time: 9:38 PM
from sqlalchemy import create_engine
import pandas as pd


class MySqlDatabase:
    def __init__(self, name, dat=None):
        self.__data = dat
        self.__table_name = name
        self.__connect = create_engine(
            "mysql+pymysql://root:root@localhost:3306/liptor?charset=utf8",
            max_overflow=0,
            pool_size=5,
            pool_timeout=30,
            pool_recycle=1).connect()

    def import_data(self):
        df = pd.DataFrame(self.__data)
        df.to_sql(self.__table_name, self.__connect, if_exists='replace', index=False)

    def export_data(self):
        return pd.read_sql("select * from app_ip;", self.__connect)


if __name__ == '__main__':
    data = [{'id': 1, 'name': 'arm', 'ip': '192.168.1.3', 'port': 3306}]
    sql = MySqlDatabase('app_ip', data)
    sql.import_data()
