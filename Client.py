from socket import *

serverName = "localhost"
serverPort = 14014
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

keep_going = True
while keep_going:
    message = input("Enter message: ")
    clientSocket.send(message.encode())
    if message == "exit":
        keep_going = False
    else:
        modifiedMessage = clientSocket.recv(2048).decode()
        print("From Server: ", modifiedMessage)
clientSocket.close()