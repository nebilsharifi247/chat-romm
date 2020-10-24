import socket
import time
import threading
nickname=input("enter chose nickame:")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",22222))
def recv():
    while True:
        try:
            message=recv(1024).decode('utf-8')
            if message  == "NICK":
                client.send(nickname.encode('utf-8'))

            else:
                print(message)
        except:
            print("an error occured")
            client.close()
            break
def write():
    while True:
        message=f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))
recvie_thared= threading.Thread(target=recv)
if time.sleep(1):
    print("connect fileds")


recvie_thared.start()

write_thead=threading.Thread(target=write)
write_thead.start()
