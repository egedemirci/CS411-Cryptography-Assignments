#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

def LFSR(C, S):
    L = len(S)
    fb = 0
    out = S[L-1]
    for i in range(0,L):
        fb = fb^(S[i]&C[i+1])
    for i in range(L-1,0,-1):
        S[i] = S[i-1]

    S[0] = fb
    return out


def FindPeriod(s):
    n = len(s)
    for T in range(1,n+1):
        chck = 0
        for i in range(0,n-T-1):
            if (s[i] != s[i+T]):
                chck += 1
                break
        if chck == 0:
            break
    if T > n/2:
        return n
    else:
        return T     
    
length = 256
print("Testing Polynomial A (p1):")
L_A = 7 
C_A = [1, 1, 0, 1, 0, 1, 0, 1]
S_A = [random.randint(0, 1) for _ in range(L_A)]  
print("Initial state:", S_A)
keystream_A = [LFSR(C_A, S_A) for _ in range(length)]
period_A = FindPeriod(keystream_A)
print("Period for p1(x):", period_A)

print("\nTesting Polynomial B (p2):")
L_B = 6  
C_B = [1, 0, 1, 0, 0, 1, 1]  
S_B = [random.randint(0, 1) for _ in range(L_B)] 
print("Initial state:", S_B)

keystream_B = [LFSR(C_B, S_B) for _ in range(length)]
period_B = FindPeriod(keystream_B)
print("Period for p2(x):", period_B)

print("\nTesting Polynomial C (p3):")
L_C = 5  
C_C = [1, 1, 0, 1, 1, 1] 
S_C = [random.randint(0, 1) for _ in range(L_C)]
print("Initial state:", S_C)

keystream_C = [LFSR(C_C, S_C) for _ in range(length)]
period_C = FindPeriod(keystream_C)
print("Period for p3(x):", period_C)

print("\nAssessment:")
print('A generates maximum period:', period_A == 2**L_A - 1)
print('B generates maximum period:', period_B == 2**L_B - 1)
print('C generates maximum period:', period_C == 2**L_C - 1)


