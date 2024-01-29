#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import requests
import BitVector

API_URL = 'http://harpoon1.sabanciuniv.edu:9999'
my_id = 28287
def get_poly():
  endpoint = '{}/{}/{}'.format(API_URL, "poly", my_id )
  response = requests.get(endpoint) 	
  a = 0
  b = 0
  if response.ok:	
    res = response.json()
    print(res)
    return res['a'], res['b']
  else:
    print(response.json())

def check_mult(c):
  #check result of part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "mult", my_id, c)
  response = requests.put(endpoint) 	
  print(response.json())

def check_inv(a_inv):
  #check result of part b
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "inv", my_id, a_inv)) 
  print(response.json())

a, b = get_poly()
##SOLUTION  

n = 8
poly = BitVector.BitVector(bitstring='111000011')
a_vector = BitVector.BitVector(bitstring=a)
b_vector = BitVector.BitVector(bitstring=b) 
q1 = a_vector.gf_multiply_modular(b_vector, poly, n)
q2 = a_vector.gf_MI(poly, n)
check_mult(q1)
print("First answer:", q1)
check_inv(q2)
print("Second answer:", q2)

