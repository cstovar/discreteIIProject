import math
import random
import sympy

def is_prime(n): #check if a given number is prime or not
    if n <= 1: #There are no negative primes
        return False
    if n == 2:
        return True  # 2 is the onlyone even prime number 
    if n % 2 == 0:
        return False  # anyother even number is not prime 
    for i in range(3, int(math.sqrt(n)) + 1, 2): #checks from 3, and the square roof of the number if any number there divides it
            return False
    return True

def find_larger(a, b): #returns an array with the two numbers ordered
    if a > b:
        return a, b
    else:
        return b, a

def generate_prime ( a, b):
    
    # prime = random.randint(a,b)
    
    # while (is_prime(prime) == False):
    #     prime = random.randint (a,b)

    b = 64 # var b with value 64
    prime = sympy.randprime(2**(b-1),2**b) # uses python function randprime an generates a number of 64bits
    return prime


'''
# Generar 2 primos aleatorios GRANDES DE "b" bits.
b = 512

p = sympy.randprime(2**(b-1),2**b)      # "randprime(x, y)" genera un número primo aleatorio en el rango [x, y).
q = sympy.randprime(2**(b-1),2**b)


# print(f"Primo de {b} bits: {p}")
# print(f"Primo de {b} bits: {q}")


# Funcion para generar llave publica "e".
def generar_coprimo(primo, bits):
    while True:
        e = random.randint(2**(bits-1), 2**bits - 1)
        if sympy.gcd(e, primo) == 1:
            return e
'''

def calc_n (a,b):
    return a*b 

def calc_phi (a,b):
    return  (a-1)*(b-1) # returns (a - 1) plus (b -1)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y #finds the greater common divisor, and s, and t, using the Euclides Algorithm

def calc_e (phi):
    flag = True
    while flag == True:
        e = random.randint(3, phi) # generates a random number between 3 and phi
        if extended_gcd(e,phi)[0] == 1: # check if gcd of the generated number and if equals 1
            flag = False #breaks the loop         
    return e #returns a number between 3 and phi, wich its gcd with phi equals 1

def calc_d (e, phi):
    gcd, x, y = extended_gcd(e, phi) #finds the greater common divisor, and s, and t, using the Euclides Algorithm
    if gcd != 1:
        raise ValueError(f"No existe inverso multiplicativo para {e} módulo {n}")
    else:
        return x % phi

def convert_to_ascii (string_): #recieves a string value a converts it to its ascii equivalent
    arr = [] #declares an array called "arr"
    for a in range (0, len(string_)): #loops the characters on the string, stops at the end of the string with method len()
        arr.append(ord(string_[a])) #adds to "arr" the ascci equivalent to each character on the string, uses "ord" python function
    return arr

def convert_to_string (arr_): # receives an array of numbers and returns its equivalent on string, accoding to ASCII code 
    string_ = "" #declares an string called "string_"
    for b in range (0, len(arr_)): #loops the numbers on the array, stops at the end of the array with method len()
        string_ += chr(arr_[b]) #adds to "string_" the ascci equivalent to each number on the string, uses "chr" python funtion
    return string_

def fast_modular_exp (b, expo, modu): #implements the fast modular pow
    assert modu > 0 and expo >= 0
    if expo == 0:
        return 1 # if the exponent equals 0, returns 1
    if expo == 1:
        return b # if the exponent equals 1, returns b
    if expo % 2 == 0:
        return fast_modular_exp((b*b) % modu, expo // 2, modu) # if the exponent is even starts recursion with ((b^2) mod m), (e/2), m
    else:
        return (fast_modular_exp(b, expo - 1, modu) * b) % modu #if the exponent is odd, starts recursion with b, (e - 1), m

def encrypt (string_, e, n):
    encr = [] #declares an array called encr
    ascii_ = convert_to_ascii(string_) #uses convert_to_ascii method to convert a string value in to its ascii equivalent

    for i in range (0, len(ascii_)): #lopps the numbers in the ascii_ array, until the end of the array with the python len() method
        c = fast_modular_exp(ascii_[i], e, n) #uses the fast_modular_exp method to calc c = (m^e) mod n, and stores it in c variable 
        encr.append(c) #adds the value in "c" to "encr" array

    return encr

def decrypt (arr_, d, n):
    decr = [] #declares an array called decr

    for i in range (0, len(arr_)): #lopps the numbers in the arr_ array, until the end of the array with the python len() method
        #m = (arr_[i] ** d) % n 
        m = fast_modular_exp(arr_[i], d, n) #uses the fast_modular_exp method to calc m = (c^d) mod n, and stores it in m variable 
        decr.append(m) #adds the value in "m" to "decr" array

    msg = convert_to_string(decr) #uses the convert_to_string method in aux class to convert the value of each number in decr to a string

    return msg

def create_tokens():
    range_1 = 20 #declares a int with a 20 value
    range_2 = 100 #declares an int with a 100 value (this two numbers if for encryption with small numbers)

    p = generate_prime(range_1, range_2)
    q = generate_prime(range_1, range_2)


    while (p == q):
        q = generate_prime(range_1, range_2 ) #for guarantee p different from q

    n = calc_n (p, q) #calculates "n" with "p" and "q"
    phi = calc_phi (p, q) #calculates "phi", with "p" and "q"
    e = calc_e(phi) #calculates "e" with "phi"
    d = calc_d(e, phi) #calculates "d", with "e" and "phi"

    tokens = [n,e,d] #stores "n" and "e" and "d" on an array called "tokens"

    return tokens

#print(create_tokens())

#print(extended_gcd(9,2))
'''
p = generate_prime(1,2)
q = generate_prime(1,2)
n = calc_n (p, q)
phi = calc_phi (p, q)
e = calc_e(phi)
d = calc_d(e, phi)




print ("p = ", p)
print ("q = ", q)
print ("n =" , n)
print ("phi = ", phi)
print ("e = ", e)
print ("d = ", d)

encry_m = encrypt ("Tenemos encripcion de 32 bits!", e, n)
print(encry_m)

decry_m = decrypt(encry_m, d, n)
print(decry_m)

#print(convert_to_string(encry_m))
'''