
# -*- coding: utf-8 -*-
from socket import *
import threading

# 服务器 IP 地址和端口号
serverPort = 8888
serverIP = '58.2.30.83'

# 创建 TCP 客户端套接字
clientSocket = socket(AF_INET, SOCK_STREAM)
# 连接服务器
clientSocket.connect((serverIP, serverPort))

# sentence = input('input lowercase sentence:')
# clientSocket.send(sentence.encode())

# modifiedSentence = clientSocket.recv(1024)
# print('from server: ', modifiedSentence.decode())

# clientSocket.close()


# 定义函数，用于接收服务器发送的消息
def receive():
    while True:
        try:
            # 接收服务器发送的消息
            data = clientSocket.recv(1024)
            print('Received:', data.decode())
        except:
            # 发生异常，关闭客户端套接字
            clientSocket.close()
            break

# 创建线程，用于接收服务器发送的消息
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 客户端输入消息，并将消息发送给服务器
while True:
    message = input()
    clientSocket.sendall(message.encode())

# 关闭客户端套接字
client_socket.close()

