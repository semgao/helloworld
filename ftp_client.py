# # 创建监听套接字
# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(ADDR)
# s.listen(3)
#
# # 连接服务器
# server_addr = ('127.0.0.1',8888)
# sockfd.connect(server_addr)
#
# class FTPServer():
#     def put():  #上传文件操作
#
#     def download():   #从服务其下载文件
#     pass
#
#
# # 客户端连接 ，创建线程
# t = Thread(target=handle, args=(,))
# t.setDaemon(True)
# t.start().

from socket import *
import sys
from time import sleep

#服务器地址
ADDR=('127.0.0.1',8888)

class FTPClient():
    def __init__(self,sock):  #sock 作为属性使用
        self.sock=sock

    #获取文件列表
    def select(self):
        self.sock.send(b"S")  #发送请求
        #等待结果
        data=self.sock.recv(128).decode()
        if data =='OK':
            #接受文件列表
            files=self.sock.recv(1024*1024).decode()
            # while True:
            #     file=self.sock.recv(1024*1024).decode()
            #     if file=='##';
            #     break
            #     print(file)
    #上传文件
    def upload(self):
        # self.sock.send(b'U')
        # if data=='OK'：
        filename=input("文件：")
        try:
            f=open(filename,'rb')
        except Exception:
            print("没有该文件")
            return
        #发送请求  U filename  *如果上传的文件名带路径需要注意
        filename=filename.split('/')[-1]
        self.sock.send(('U'+filename)).decode()
        #等待反馈
        data=self.sock.recv(128).decode()
        if data=='OK':
            data=f.read(1024)
            if not data:
                sleep(0.1)
                self.sock.send(b'##')
                break
            self.
        else:
            print(data)
    #下载文件
    def download(self):
        #输入文件名
        #发送请求
        #等待反馈
        #循环接收文件，并写入



def main():
    sock=socket()
    sock.connect(ADDR)

    ftp=FTPClient()         #实例化对象用于调用请求函数

    #循环发送请求
    while True:
        print("\n==========COMMAND==========")
        print("****       select      ****")
        print("****       download    ****")
        print("****       upload      ****")
        print("****        quit       ****")
        print("===========================")

        cmd = input("Command:")
        if cmd.strip()=='select':
            ftp.select()
        elif cmd.strip()=='upload':
            ftp.upload()
        elif cmd.strip()=='download':
            ftp.download()



        sock.send(cmd.encode())
if __name__ == '__main__':
    main()