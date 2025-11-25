import socket, threading

clients = []

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            for c in clients:
                if c != client:
                    c.send(msg)
        except:
            break
    clients.remove(client)
    client.close()

server = socket.socket()
server.bind(("0.0.0.0", 12345))
server.listen(5)
print("Server started...")

while True:
    client, addr = server.accept()
    print("Client connected:", addr)
    clients.append(client)
    threading.Thread(target=handle, args=(client,)).start()


#Server started...
#Client connected: ('127.0.0.1', 50124)
#Client connected: ('127.0.0.1', 50126)
#Received: hello
#Received: hi everyone
#Received: how are you? 





