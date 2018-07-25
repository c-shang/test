# coding:utf8
# created at 2018/7/24.

import threading

print('are you ok?')

def worker():
    print('I\' fine')
    t = threading.current_thread()
    print(t.getName())

t = threading.current_thread()
print(t.getName())
#主线程

new_t = threading.Thread(target=worker,name='new_thread')
new_t.start()
#子线程