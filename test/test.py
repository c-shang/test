# coding:utf8
# created at 2018/7/24.

from flask import Flask,current_app

app = Flask(__name__)

ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()

#flask中的上下文(皆对象)
#*应用上下文 对flask封装
#*请求上下文 对Request封装
#Flask -> AppContext
#Request -> RequestContext
#离线应用、单元测试

# with语句
# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']

#1.连接数据库
#2.sql
#3.释放资源

#实现上下文协议的对象使用with
#上下文管理器
#__enter__ __exit__

#文件读写
# f = open(r'/tmp/abc.txt')


#as后面的一定不是上下文管理器，为None


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource connection')

    def query(self):
        print('query data')

with MyResource() as resource:
    resource.query()