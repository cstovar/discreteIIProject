import socket
import rsa
import aux_p
print ("client")
ipServer = "localhost"
portServer = 9798
device_name = socket.gethostname()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ipServer, portServer))

public_key_str = client.recv(4096).decode('utf-8') #receives a message with the tokens from server 
server_tokens = [int(x) for x in public_key_str.split(',')] #adds the server tokens to an array 


print("Server: ", (ipServer,portServer))

tokens_cli = rsa.create_tokens() #creates tokens for the client, using the rsa class, create_tokens method

n_cli = int(tokens_cli[0]) #On the variable n_cli stores "n" for client
public_key_cli = int(tokens_cli[1]) #On the variable public_key_cli stores "e" for client
private_key_cli = int(tokens_cli[2]) #On the varibale private_key_cli stores "d" for client


public_key_str_cli = f"{public_key_cli},{n_cli}" # adds the client tokens to a string
client.send(public_key_str_cli.encode('utf-8')) #sends the tokens to the server 



while True:
    #For send message
    msg = input("--") #reads a mesaage from keyboard
    encr_ = rsa.encrypt(msg, server_tokens[0], server_tokens[1]) #uses encrypt method from rsa, to encrypt the message with tokens from server (e, n)
    msg_enc = ','.join(str(x) for x in encr_) #converts the array of numbers with the encrypted message to a string, separated by comma
    client.send(msg_enc.encode('utf-8')) #encodes with "utf-8" (for effiecient storage) and sends the encrypted message to server

    #For receive message
    server_reply = client.recv(4096) #receives a encrypted message from server 
    reply_ = server_reply.decode('utf-8') #decodes the message and stores it in "reply_" variable 
    encry_m = aux_p.string_to_array(reply_) #uses the "aux_p" class, with the string_to_array method to convert the string separated by comma into an array
    legible_m = rsa.decrypt(encry_m, private_key_cli, n_cli) #uses the decrypt method in "rsa" class to decrypt the message using (private_key, n) 

    if legible_m == 'exit': #is a key word to finish the programm execution
        break
    print("From Server ->", legible_m) #prints the legible menssage after decrypt it
client.close() #closes the client session
