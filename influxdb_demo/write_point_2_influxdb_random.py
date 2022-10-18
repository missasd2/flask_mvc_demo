"""
随机模拟不同数值，写入influxdb
"""
import datetime
import random
import time


host_list = ["server01", "server02", "server03", "server04"]
region_list = ["us-west", "us-east", "cn-north", "cn-south", "cn-east"]

value =  {'time_stamp': '2022-10-18, 23:11:39', 'count_num_random': 10}

from influxdb import InfluxDBClient
client = InfluxDBClient('192.168.25.136', 8086, username='sw', password='123456')  # 连接数据库
client.create_database('example')  # 创建数据库


get_epoch_time = datetime.datetime(2022, 10, 18, 0, 0, 1).timestamp() # 1666022401.0
timeArray = time.localtime(get_epoch_time) # timeArray
get_y_m_d_time = time.strftime("%Y-%m-%d, %H:%M:%S", timeArray)


def generate_random_time():
    year = 2022
    month = 10
    day = 18
    hour = random.randint(0, 12)
    minute = random.randint(0, 59)
    seconds = random.randint(0, 59)
    get_epoch_time = datetime.datetime(year, month, day, hour, minute, seconds).timestamp()  # 1666022401.0
    timeArray = time.localtime(get_epoch_time)  # timeArray
    get_y_m_d_time = time.strftime("%Y-%m-%d, %H:%M:%S", timeArray)
    return get_y_m_d_time

def generate_random_points():
    point = [  # 待写入数据库的点组成的列表
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": random.choice(host_list),
                "region": random.choice(region_list)
            },
            "time": generate_random_time(),
            "fields": {
                "value": float("%.2f" % random.random())
            }
        }
    ]
    # print(point, "123")
    return point


def main():
    while True:
        # poin = ,
        client.write_points(points=generate_random_points(), database='example', time_precision="s")  # 将这些点写入指定database

# 查询刚刚写入的点


if __name__ == '__main__':
    print(generate_random_points())
    main()
