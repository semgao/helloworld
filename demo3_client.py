"""
ftp 文件服务 客户端
"""
from socket import *
import sys
from time import sleep

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 请求功能
class FTPCient:
    def __init__(self,sock):
        self.sock = sock

    # 获取文件列表
    def select(self):
        self.sock.send(b"S") # 发送请求
        # 等待结果 等 Yes or No
        data = self.sock.recv(128).decode()
        if data == 'OK':
            # 接收文件列表
            files = self.sock.recv(1024*1024*10).decode()
            print(files)
            # while True:
            #     file = self.sock.recv(128).decode()
            #     if file == '##':
            #         break
            #     print(file)
        else:
            print(data)

    # 上传文件
    def upload(self):
        i=1
        while i <=4:
            filename = input("文件：")
            try:
             f = open(filename,'rb')
             i+1
            except Exception:
                print("没有该文件")
                return
        # 发送请求  U filename
        filename = filename.split('/')[-1] # 提取真正的文件名
        self.sock.send(("U "+filename).encode())
        # 等待反馈
        data = self.sock.recv(128).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sock.send(b'##')
                    break
                self.sock.send(data)
            f.close()
        else:
            print(data)

    # # 下载文件
    # def download(self):
    #     filename = input("文件：")
    #     self.sock.send(("D " + filename).encode())
    #     # 等待反馈
    #     data = self.sock.recv(128).decode()
    #     if data == "OK":
    #         f = open(filename, 'wb')
    #         while True:
    #             data = self.sock.recv(1024)
    #             if data == b'##':
    #                 break
    #             f.write(data)
    #         f.close()
    #     else:
    #         print(data)

    def quit(self):
        self.sock.send(b'Q')
        self.sock.close()
        sys.exit("谢谢使用")

def main():
    sock = socket()
    sock.connect(ADDR)

    # 实例化对象用来调用请求函数
    ftp = FTPCient(sock)

    # 循环发送请求
    while True:
        print("\n==========COMMAND==========")
        print("****       select      ****")
        print("****       upload      ****")
        print("****      download     ****")
        print("****        quit       ****")
        print("===========================")

        cmd = input("Command:")
        if cmd.strip() == "select":
            ftp.select()
        elif cmd.strip() == 'upload':
            ftp.upload()
        elif cmd.strip() == 'download':
            ftp.download()
        elif cmd.strip() == 'quit':
            ftp.quit()
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()