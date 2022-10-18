"""
json转换为实体类
"""
import json
class Student(object):
    def __init__(self, name, age, score, reward):
        self.name = name
        self.age = age
        self.score = score
        self.reward = reward


def dict2student(d):
    return Student(d['name'], d['age'], score=d['score'], reward=d['reward'])


json_str = '{"name": "Bob", "age": 20, "score": 88, "reward": ["三好学生", "优秀团干", "最佳辩手"]}'
student = json.loads(json_str,object_hook=dict2student)
print(type(student))
print(student.name)
