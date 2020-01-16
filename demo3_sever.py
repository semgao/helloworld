"""
ftp 文件服务器，服务端
env: python3.6
多线程并发，socket
"""

from socket import *
from threading import Thread
import sys
import os
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/桌面/未学习/day09/" # 文件库位置

# 文件处理功能
class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    # 发送文件列表
    def select(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        file_list = '\n'.join(files)
        self.connfd.send(file_list.encode())
        # for file in files:
        #     self.connfd.send(file.encode())
        #     sleep(0.1)
        # self.connfd.send(b'##')

    # 处理上传
    def upload(self,filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接受文件
        f = open(FTP + filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 处理下载
    def download(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            # 打开失败文件不存在
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()


    # 处理客户端请求
    def run(self):
        # 循环接受请求
        while True:
            data = self.connfd.recv(1024).decode()
            print("Request:",data)
            if not data or data == 'Q':
                return # 线程结束
            elif data == 'S':
                self.select()
            elif data[0] == 'U':
                filename = data.split(' ')[-1]
                self.upload(filename)
            elif data[0] == 'D':
                filename = data.split(' ')[-1]
                self.download(filename)

# 网络功能
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    print('Listen the port 8888...')
    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 客户端连接 ，创建线程
        t = FTPServer(c)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()