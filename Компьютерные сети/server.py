#!/bin/python3
import socket
import threading

# Connection Data
host = '127.0.0.1' #прописала IP
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()  # сокет напрвлен на прием входящих сообщений

# Lists For Clients and Their Nicknames #создаем  2 списка 
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):             # сообщения рассылаются всем участником чата
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:                       # когда получаем сообщения, то отправляем всем участником чата
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:                       #если сообщение не доставленно, клиент удаляется из чата
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():                 #функция сервера (сам сервер)
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)  #добавляются новые участники чата

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))  #каждое сообщения напрвляется в отдельный чат
        thread.start()

print("Server if listening...")
receive()
