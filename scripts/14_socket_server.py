#! -*- coding:utf-8 -*-

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def test_socket():
    #1.创建套接字对象并指定使用哪种传输服务
    #family=AF_INET -- IPV4
    #family=AF_INET6 -- IPV6
    #type=SOCK_STEAM TCP套接字
    #type=SOCK_DGRAM UDP套接字
    #type=SOCK_RAW 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    #2.绑定IP地址和端口
    #同时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.8.111', 6789))
    #3.开启监听 监听客户端连接到服务器
    #参数512可以理解连接队列大小
    server.listen(512)
    print('server start')
    while True:
        #4.通过循环接收客户端的连接并做出相应的处理
        #accept方法是一个阻塞方法 如果没有客户端连接到服务端不会执行后续代码
        #accept方法返回一个元祖其中第一个为客户端对象
        #第二个是链接到服务器的客户端地址（由IP+端口组成）
        client, addr = server.accept()
        print(str(addr) + 'connected')
        #5.发送数据
        client.send(str(datetime.now()).encode("utf-8"))
        #6.断开链接
        client.close()


if __name__ == "__main__":
    test_socket()
