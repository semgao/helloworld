"""
两个线程一个打印1-52，另一个打印A-Z，两个线程同时进行
要求：打印出12A34B56C78D...5152Z

"""

from threading import Thread,Lock
import os
import sys



# def value():
#     while True:
#         lock.acquire()   #上锁
#         if a!=b:
#             print("a=%d,b=%d"%(a,b))
#         lock.release()   #解锁
# def fun1()
lock1=Lock()
lock2=Lock()


def fun1(n):
    for i in range(26):
        lock1.acquire()   #上锁
        print(n,end='')
        print(n+1,end='')
        n += 2
        lock2.release()   #解锁

def fun2():
    for i in range(26):
        lock2.acquire()  # 上锁
        print(chr(i+ord('A')))
        lock1.release()  # 解锁


t1=Thread(target=fun1,args=(1,))
t2=Thread(target=fun2)
lock2.acquire()

t1.start()
t2.start()