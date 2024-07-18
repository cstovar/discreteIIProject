import socket
import rsa
import aux_p
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",9798))
s.listen(5)
print("Server")
print("Servidor de Chat\n")
active, addr = s.accept()


tokens_ = rsa.create_tokens() #creates tokens for server, using the rsa class, create_tokens method

n_ = int(tokens_[0]) #On the variable n_ stores "n" for server
public_key = int(tokens_[1]) ##On the variable public_key stores "e" for server
private_key = int(tokens_[2]) #On the varibale private_key stores "d" for server

public_key_str = f"{public_key},{n_}" # adds the server token to a string
active.send(public_key_str.encode('utf-8')) # sends the tokens to the client 

public_key_str_cli = active.recv(4096).decode('utf-8') #receives a message with the tokens from client 
client_tokens = [int(x) for x in public_key_str_cli.split(',')] #adds the server tokens to an array 

while True:
    #For receive message
    client_reply = active.recv(4096) #receives a encrypted message from client 
    reply_ = client_reply.decode('utf-8') #decodes the message and stores it in "reply_" variable 
    encry_m = aux_p.string_to_array(reply_) #uses the "aux_p" class, with the string_to_array method to convert the string separated by comma into an array
    legible_m = rsa.decrypt(encry_m, private_key, n_)  #uses the decrypt method in "rsa" class to decrypt the message using (private_key, n) 
    print ("From client --", legible_m) #prints the legible menssage after decrypt it

    #For send message
    server_msg = input("->") #reads a mesaage from keyboard
    encr_s = rsa.encrypt(server_msg, client_tokens[0], client_tokens[1]) #uses encrypt method from rsa, to encrypt the message with tokens from client (e, n)
    server_msg_encr = ','.join(str(x) for x in encr_s) #converts the array of numbers with the encrypted message to a string, separated by comma
    active.send(server_msg_encr.encode('utf-8')) #encodes with "utf-8" (for effiecient storage) and sends the encrypted message to client
active.close() #closes the server session