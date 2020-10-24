#Created By nebil sharifi
#Socket programing
#socket chatrom
import socket
import time
#imported libary  socket
#imported libary  threading
#imported libary System
import threading
import sys
host="127.0.0.1"
port=22222
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#method socket tcp connection
server.bind((host,port))
server.listen(80)
clients=[]
nicknames=[]
def broadcast(messsage):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nicname=nicknames[index]
            broadcast(f"{nickname} left the chat".encode('utf-8'))
            nicknames.remove(nickname)
            break

def recvevie(*args):
    while  True:
        client,adress=server.accept()


        print(f"connected with{str(adress)}")


        client.send("NICK".encode('utf-8'))
        nickame=client.recv(1024).decode('utf-8')
        clients.append(client)
        print(f"nickame of the client is {client}")
        broadcast(f"{nickame}joined the chat!")
        client.send("connected the server !").encode('utf-8')

        Thread=threading.Thread(target=handle, args=(client,))
        Thread.start()


print("server is listening")
data=recvevie()
print(data)
print("hi")
