import random
import time

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

def producer_demo():
    # 假设生产的消息为键值对（不是一定要键值对），且序列化方式为json
    producer = KafkaProducer(
        bootstrap_servers=['192.168.25.136:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    # 发送三条消息
    for i in range(0, 3):
        future = producer.send(
            'kafka_demo',
            key='count_num',  # 同一个key值，会被送至同一个分区
            value=str(i))  # 向分区1发送消息
        print("send {}".format(str(i)))
        try:
            future.get(timeout=10) # 监控是否发送成功           
        except kafka_errors:  # 发送失败抛出kafka_errors
            traceback.format_exc()


def producer_demo_random():
    producer = KafkaProducer(
        bootstrap_servers=['192.168.25.136:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    while True:
        num = random.randint(3, 10)
        time.sleep(num)
        # '2022-10-18, 21:45:56'
        message = {"time_stamp": time.strftime("%Y-%m-%d, %H:%M:%S", time.localtime()),
                   "count_num_random": num
                   }
        print(message)
        producer.send("kafka_demo_random", key="my_key", value=message)

if __name__ == '__main__':
    producer_demo_random()