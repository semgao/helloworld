"""
tcp客户端流程
"""
from socket import *

# 默认情况就是tcp套接字
sockfd = socket()

# 连接服务器
server_addr = ('127.0.0.1',8000)
sockfd.connect(server_addr)

# 发收消息
while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode()) # 要发送字节串
    # if msg == '##':
    #     break
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()