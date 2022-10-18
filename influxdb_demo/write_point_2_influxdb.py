"""
单个点
"""

import datetime
import time

value =  {'time_stamp': '2022-10-18, 23:11:39', 'count_num_random': 10}

from influxdb import InfluxDBClient
client = InfluxDBClient('192.168.25.136', 8086, username='sw', password='123456')  # 连接数据库
client.create_database('example')  # 创建数据库


get_epoch_time = datetime.datetime(2022, 10, 18, 0, 2, 1).timestamp() # 1666022401.0
timeArray = time.localtime(get_epoch_time) # timeArray
get_y_m_d_time = time.strftime("%Y-%m-%d, %H:%M:%S", timeArray)

points = [ # 待写入数据库的点组成的列表
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": get_y_m_d_time,
        "fields": {
            "value": 0.65
        }
    }
]
client.write_points(points, database='example', time_precision="s")  # 将这些点写入指定database
# 查询刚刚写入的点
result = client.query('select value from cpu_load_short;', database='example')
print(result)
