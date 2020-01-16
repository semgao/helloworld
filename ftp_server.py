"""
ftp 文件服务器，服务端


"""
from socket import *
from threading import Thread
import sys,os
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP ='/home/tarena/桌面/未学习/day09/'

#文件处理功能
class FTPServer():
    def __init__(self,connfd):
        super().__init__()
        self.connfd=connfd
    #发送文件列表
    def select(self):
        files=os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        file_list='\n'.join(file_list.encode())
        # for file in files:
        #     self.connfd.send(file.encode())
        # self.connfd.send(b'##')
    #写入文件
    def Write(self):

        #判断文件是否存在
        #响应客户端消息
        #写入客户端发送的文件，并存储
        #
    #下载文件
    def Download(self):
        #判断文件是否存在
        #循环读文件并发送

    def run(self):
        #循环接受请求
        while True:
            data=self.connfd.recv(1024).decode()
            print("Request:",data)
            if data=='S':
                self.select()
            elif data=='U':
                self.Write()
            elif data=='D':
                self.Download()

#网络功能
def main():
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
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

