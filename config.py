# 数据库的配置文件写在config.py文件中：
DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='asd159357'
HOST='104.225.157.227'
PORT='3306'
DATABASE='flask_ex'
SQLALCHEMY_DATABASE_URI=DIALECT+'://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS=False