import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ") #запрос имени участника чата

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555)) #прописываем IP

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii') #получаес запрос на введение  ника
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message) #печатаются сообщения от других участников чата
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input('')) #указывается ник запрощенный выше
        client.send(message.encode('ascii')) #сообщение от участника чата с ником выше

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive) #паток на прием сообщений
receive_thread.start()

write_thread = threading.Thread(target=write)  #паток для написания сообщений
write_thread.start()