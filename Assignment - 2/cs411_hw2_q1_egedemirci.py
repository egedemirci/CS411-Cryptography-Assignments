#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1

import random
import requests

API_URL = 'http://harpoon1.sabanciuniv.edu:9999/'

# Change your id here
my_id = 28287

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def getQ1():
  endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    print(res)
    n, t = res['n'], res['t']
    return n,t
  else: print(response.json())

def checkQ1a(order):   #check your answer for Question 1 part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
  response = requests.put(endpoint) 	
  print(response.json())

def checkQ1b(g):  #check your answer for Question 1 part b
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())

def checkQ1c(gH):  #check your answer for Question 1 part c
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())


n, t = getQ1()
answer = phi(n)
print("Number of elements in the group:", answer)
checkQ1a(answer)



def find_elements_coprime_to_n(n):
    coprime_elements = {i for i in range(1, n) if gcd(i, n) == 1}
    return coprime_elements

def find_generator(n, coprime_elements):
    for candidate in range(2, n):
        generated_elements = {pow(candidate, exp, n) for exp in range(1, n)}
        if generated_elements == coprime_elements:
            print(f"Potential Generator: {candidate}")
            break

coprime_to_n = find_elements_coprime_to_n(n)
find_generator(n, coprime_to_n)
checkQ1b(15)


def find_subgroup_elements(n, t):
    return {i for i in range(1, n) if pow(i, t, n) == 1}

def is_subgroup_generator(g, n, t):
    if all(pow(g, k, n) != 1 for k in range(1, t)) and pow(g, t, n) == 1:
        return True
    return False

subgroup_elements = find_subgroup_elements(n, t)
for element in subgroup_elements:
    if is_subgroup_generator(element, n, t):
        print(f"Generator of the subgroup: {element}")
        checkQ1c(element)
        break

