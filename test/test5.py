# coding:utf8
# created at 2018/7/25.

from werkzeug.local import Local
import threading
import time

class A:
    b = 1

my_obj = Local()    #用字典去保存不同线程的id号，从而实现线程之间的隔离
my_obj.b = 1

def worker():
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))

new_t = threading.Thread(target=worker,name='new_thread')
new_t.start()
time.sleep(1)
print('in main thread b is:' +  str(my_obj.b))