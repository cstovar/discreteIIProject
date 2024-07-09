import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",9798))
s.listen(5)
print("Server")
print("Servidor de Chat\n")
active, addr = s.accept()

while True:
    client_reply = active.recv(1024)
    print ("--", client_reply.decode('utf-8'))
    server_msg = input("->")
    active.send(server_msg.encode('utf-8'))
active.close()