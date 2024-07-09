import math
import random

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the onlyone even prime number 
    if n % 2 == 0:
        return False  # anyother even number is not prime 
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_larger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

def generate_prime ( a, b):
    
    prime = random.randint(a,b)
    
    while (is_prime(prime) == False):
        prime = random.randint (a,b)
    
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
    return  (a-1)*(b-1)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def calc_e (phi):
    flag = True
    while flag == True:
        e = random.randint(3, phi)
        if extended_gcd(e,phi)[0] == 1:
            flag = False           
    return e

def calc_d (e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"No existe inverso multiplicativo para {e} módulo {n}")
    else:
        return x % phi

def convert_to_ascii (string_):
    arr = []
    for a in range (0, len(string_)):
        arr.append(ord(string_[a]))
    return arr

def convert_to_string (arr_):
    string_ = ""
    for b in range (0, len(arr_)):
        string_ += chr(arr_[b])
    return string_

def encrypt (string_, e, n):
    encr = []
    ascii_ = convert_to_ascii(string_)

    for i in range (0, len(ascii_)):
        c = (ascii_[i] ** e) % n
        encr.append(c)

    return encr

def decrypt (arr_, d, n):
    decr = []

    for i in range (0, len(arr_)):
        m = (arr_[i] ** d) % n 
        decr.append(m)

    msg = convert_to_string(decr)

    return msg

range_1 = 20
range_2 = 100

p = generate_prime(range_1, range_2)
q = generate_prime(range_1, range_2)


while (p == q):
    q = generate_prime(range_1, range_2 )


n = calc_n (p, q)
phi = calc_phi (p, q)
e = calc_e(phi)
d = calc_d(e, phi)

print (p)
print(q)
print ("n =", n)
print ("phi = ", phi)
print ("e = ", e)
print ("d = ", d)

encry_m = encrypt ("Hola, como estas?", e, n)
print(encry_m)

decry_m = decrypt(encry_m, d, n)
print(decry_m)












