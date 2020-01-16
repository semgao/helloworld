"""
根据多进程网络并发的模型和思想，完成Thread的多线程并发
重点代码
"""

from socket import *
from threading import Thread
import sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理函数
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.send(b'OK')
    connfd.close()


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

print('Listen the port 8888...')
# 循环等待客户端连接
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 客户端连接 ，创建线程
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()