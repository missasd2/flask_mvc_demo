FROM python:3.8
WORKDIR /root/project/pythonproject/flask_demo_2

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]

