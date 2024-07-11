import socket
import rsa
import aux_p
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",9798))
s.listen(5)
print("Server")
print("Servidor de Chat\n")
active, addr = s.accept()


tokens_ = rsa.create_tokens()

n_ = int(tokens_[0])
public_key = int(tokens_[1])
private_key = int(tokens_[2])

public_key_str = f"{public_key},{n_}" # adds the server token to a string
active.send(public_key_str.encode('utf-8')) # sends the tokens to the client 

public_key_str_cli = active.recv(1024).decode('utf-8') #receives a message with the tokens from client 
client_tokens = [int(x) for x in public_key_str_cli.split(',')] #adds the server tokens to an array 

while True:
    client_reply = active.recv(1024)
    reply_ = client_reply.decode('utf-8')

    encry_m = aux_p.string_to_array(reply_)
    legible_m = rsa.decrypt(encry_m, private_key, n_)
    print ("From client --", legible_m)


    server_msg = input("->")
    encr_s = rsa.encrypt(server_msg, client_tokens[0], client_tokens[1])
    server_msg_encr = ','.join(str(x) for x in encr_s)
    active.send(server_msg_encr.encode('utf-8'))
active.close()