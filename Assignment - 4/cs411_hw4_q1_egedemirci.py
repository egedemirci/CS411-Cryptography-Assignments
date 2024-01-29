#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import requests
from random import randint

API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 28287

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def RSA_Oracle_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id)) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())

def RSA_Oracle_Query(c_):
  response = requests.get('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Query", my_id, c_)) 
  print(response.json())
  m_= ""
  if response.ok:	m_ = (response.json()['m_'])
  else: print(response)
  return m_

def RSA_Oracle_Checker(m):
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Checker", my_id, m))
  print(response.json())

# Get the ciphertext, modulus, and public key exponent from the Oracle
c, N, e = RSA_Oracle_Get()

# Select a random plaintext value choP (not equal to the actual plaintext). I chose 7 in this case.
choP = 7
# Encrypt choP using the public key (choC = choP^e mod N)
choC = pow(choP, e, N) 

# Create a new ciphertext to query the Oracle with (sendC = choC * C mod N)
sendC = (choC * c) % N 
# Query the Oracle with the modified ciphertext and receive the corresponding plaintext
sendM = RSA_Oracle_Query(sendC) 

# Decrypt the original message (m = sendM * modinv(choP, N) mod N)
m = (sendM * modinv(choP, N)) % N 

print("Decrypted numeric value of m:", m)
# Convert the numeric message m into readable string format
message = m.to_bytes((m.bit_length() // 8 + 1), byteorder="big").decode()
print("Decrypted message:", message)

# Check the correctness of the decrypted message
RSA_Oracle_Checker(message)

