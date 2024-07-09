import socket
print ("client")
ipServer = "localhost"
portServer = 9798
device_name = socket.gethostname()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipServer, portServer))
print("Server: ", (ipServer,portServer))

while True:
    msg = input("--")
    client.send(msg.encode('utf-8'))
    server_reply = client.recv(1024)
    if msg == 'exit':
        break
    print("->", server_reply.decode('utf-8'))
client.close()
