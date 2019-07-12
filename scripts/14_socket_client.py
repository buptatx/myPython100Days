#! -*- coding:utf-8 -*-

from base64 import b64decode
from socket import socket
from json import loads


def test_socket_client():
    client = socket()
    client.connect(('192.168.8.111', 6789))

    print(client.recv(1024))
    client.close()


def socket_download_pic_client():
    client = socket()
    client.connect(('192.168.8.111', 6790))
    #定义一个保存二进制数据的对象
    in_data = bytes()
    #由于不知道服务器发送的数据大小，每次接受1024
    data = client.recv(1024)

    loop_time = 1
    while data:
        in_data += data
        print("[%d] load data from server, current recv data size:%d" \
            % (loop_time, len(in_data)))
        data = client.recv(1024)
        loop_time += 1

    #将收到的二进制数据解码成JSON字符串并转换成字典
    #loads将Json字符串转化为json字典对象
    my_dict = loads(in_data.decode("utf-8"))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')

    with open('../data/res_' + filename, "wb") as mf:
        #将base64格式的数据解码成二进制并写入文件
        mf.write(b64decode(filedata))
    print('pic local store finish')


if __name__ == "__main__":
    #test_socket_client()
    socket_download_pic_client()