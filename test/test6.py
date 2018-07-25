# coding:utf8
# created at 2018/7/25.

import threading
import time
from werkzeug.local import LocalStack

s = LocalStack()
# s.push(1)
# print(s.top)
# print(s.pop())
# print(s.top)

#栈是后进先出
#
# s.push(1)
# s.push(2)
# print(s.top)
# print(s.top)
# print(s.pop())
# print(s.top)

my_stack = LocalStack()
my_stack.push(1)
print('In main thread after push,value is:' + str(my_stack.top))

def worker():
    print('In new thread before push,value is:' + str(my_stack.top))
    my_stack.push(2)
    print('In new thread after push,value is:' + str(my_stack.top))

new_t = threading.Thread(target=worker,name='new_thread')
new_t.start()

time.sleep(1)
print('finally, in main thread value is:' + str(my_stack.top))