import socket
import rsa
import aux_p
print ("client")
ipServer = "localhost"
portServer = 9798
device_name = socket.gethostname()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipServer, portServer))

public_key_str = client.recv(1024).decode('utf-8') #receives a message with the tokens from server 
server_tokens = [int(x) for x in public_key_str.split(',')] #adds the server tokens to an array 


print("Server: ", (ipServer,portServer))

tokens_cli = rsa.create_tokens()

n_cli = int(tokens_cli[0])
public_key_cli = int(tokens_cli[1])
private_key_cli = int(tokens_cli[2])


public_key_str_cli = f"{public_key_cli},{n_cli}" # adds the client tokens to a string
client.send(public_key_str_cli.encode('utf-8')) #sends the tokens to the server 



while True:
    msg = input("--")
    encr_ = rsa.encrypt(msg, server_tokens[0], server_tokens[1])
    msg_enc = ','.join(str(x) for x in encr_)
    client.send(msg_enc.encode('utf-8'))


    server_reply = client.recv(1024)
    reply_ = server_reply.decode('utf-8')
    encry_m = aux_p.string_to_array(reply_)
    legible_m = rsa.decrypt(encry_m, private_key_cli, n_cli)

    if legible_m == 'exit':
        break
    print("From Server ->", legible_m)
client.close()
