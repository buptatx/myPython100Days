#! -*- coding:utf-8 -*-

from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread


class FileTransferHandler(Thread):
    def __init__(self, client, filename, data):
        super().__init__()
        self._client = client
        self._data = data
        self._filename = filename

    def run(self):
        my_dict = dict()
        my_dict['filename'] = self._filename
        #json是纯文本不能携带二进制数据
        #所以图片的二进制数据要处理为base64
        my_dict['filedata'] = self._data
        json_str = dumps(my_dict)
        print("send start")
        self._client.send(json_str.encode("utf-8"))
        print("file transfer finished, prepare to close connection")
        self._client.close()


def socket_server(filename):
    #1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    #2.绑定IP地址和端口
    server.bind(('192.168.8.111', 6790))
    #3.开始监听
    server.listen(512)
    print('server start')
    with open('../data/' + filename , 'rb') as f:
        #将二进制数据转化为base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')

    #4.循环处理客户端请求
    #每个客户端请求，创建一个线程进行处理
    while True:
        client, addr = server.accept()
        print("%s connect, prepare to transfer file" % str(addr))
        #启动一个线程处理客户端请求
        FileTransferHandler(client, filename, data).start()


if __name__ == "__main__":
    socket_server('ban.jpeg')
