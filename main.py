from socket import *
import threading


def handle_client(connectionSocket, addr):
    keep_going = True
    while keep_going:
        message = connectionSocket.recv(2048).decode()
        if message == "exit":
          keep_going = False
        # return a speicfic message in uppercase
        elif message.startswith("upper:") and message.endswith(";"):
            toupper_message = message[6:-1].upper()
            connectionSocket.send(toupper_message.encode())
        # return a specific message in lowercase
        elif message.startswith("lower:") and message.endswith(";"):
            tolower_message = message[6:-1].lower()
            connectionSocket.send(tolower_message.encode())
        # return a specific message in titlecase
        elif message.startswith("title:") and message.endswith(";"):
            totitle_message = message[6:-1].title()
            connectionSocket.send(totitle_message.encode())
        # return a specific message in reverse
        elif message.startswith("reverse:") and message.endswith(";"):
            reverse_message = message[8:-1][::-1]
            connectionSocket.send(reverse_message.encode())
        # return a specific message in alternating case
        elif message.startswith("alternating:") and message.endswith(";"):
            alternating_message = message[12:-1][::2].lower() + message[12:-1][1::2].upper()
            connectionSocket.send(alternating_message.encode())
        else:
            #missing_message = "Missing command or semicolon"
            fail_message = "Missing command or semicolon"
            connectionSocket.send(fail_message.encode())
            print("From: ", addr[0])
            print("Received: ", message)

    connectionSocket.close()
serverPort = 14014
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready")
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()



