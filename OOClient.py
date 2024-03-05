from socket import *


def send_method(method, serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(method.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    return clientSocket


def send_numbers(numbers, clientSocket):
    clientSocket.send(numbers.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    clientSocket.close()


serverName = 'localhost'
serverPort = 12000
method = input("Enter command (random, add, subtract): ")
clientSocket = send_method(method, serverName, serverPort)
numbers = input()
send_numbers(numbers, clientSocket)