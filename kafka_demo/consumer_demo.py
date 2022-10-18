"""
消费者-demo
"""

from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json


def consumer_demo():
    consumer = KafkaConsumer(
        'kafka_demo_random',
        bootstrap_servers='192.168.25.136:9092',
        group_id='test'
    )
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
            )
        )


if __name__ == '__main__':
    consumer_demo()