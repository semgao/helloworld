"""
fork_server.py  基于fork的多进程网络并发
重点代码
"""
from socket import *
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端事件
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

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print('Listen the port 8888...')
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("服务器退出")
        s.close()
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # 客户端连接后，新的进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c) # 处理客户端请求
        os._exit(0) # 子进程处理完客户端事件就退出
    else:
        c.close()