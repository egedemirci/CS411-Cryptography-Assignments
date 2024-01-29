#!/usr/bin/env python
# coding: utf-8

# In[8]:


import copy 

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

def PolPrune(P):
    n = len(P)
    i = n-1
    while (P[i] == 0):
        del P[i]
        i = i-1
    return i

def PolDeg(P):
    n = len(P)
    i = n-1
    while (P[i] == 0):
        i = i-1
    return i

# P gets Q
def PolCopy(Q, P):
    degP = len(P)
    degQ = len(Q)
    if degP >= degQ:
        for i in range(0,degQ):
            Q[i] = P[i]
        for i in range(degQ, degP):
            Q.append(P[i])
    else: # degP < deqQ
        for i in range(0,degP):
            Q[i] = P[i]
        for i in range(degP, degQ):
            Q[i] = 0
        PolPrune(Q)           

def BM(s):
    n = len(s)

    C = []
    B = []
    T = []
    L = 0
    m = -1
    i = 0
    C.append(1)
    B.append(1)

    while(i<n):
        delta = 0
        clen = len(C)
        for j in range(0, clen):
            delta ^= (C[j]*s[i-j])
        if delta == 1:
            dif = i-m
            PolCopy(T, C)
            nlen = len(B)+dif
            if(clen >= nlen):
                for j in range(dif,nlen):
                    C[j] = C[j] ^ B[j-dif]
            else: # increase the degree of C
                for j in range(clen, nlen):
                    C.append(0)
                for j in range(dif, nlen):
                    C[j] = C[j] ^ B[j-dif]
            PolPrune(C)
            if L <= i/2:
                L = i+1-L
                m = i
                PolCopy(B, T)  
        i = i+1    
    return L, C

def ASCII2bin(msg):
    M_i = []
    Mlen = len(msg)
    for i in range(0,Mlen):
        ascii_no = ord(msg[i])
        ascii_bin = bin(ascii_no)
        char_len = len(ascii_bin)
        if(char_len<9):
            for j in range(0,9-char_len):
                M_i.append(0)
        for j in range(2,char_len):
            M_i.append(int(ascii_bin[j]))
    return M_i

def bin2ASCII(msg):
    res = list()
    for i in range(len(msg)//7):
        bins = msg[:7]
        str_bin = ''.join(str(x) for x in bins)
        res.append(chr(int(str_bin,2)))
        msg = msg[7:]
    return "".join(res)

def perform_xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

ctext=[0, 0, 1, 0, 0, 0, 1, 1, 0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1,1,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1,0,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,1,0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1,0,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,0, 1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1]

known_plaintext_end = "Erkay Savas"
binary_ptext_end = ASCII2bin(known_plaintext_end)
num_bits_end = len(binary_ptext_end)
ctext_end_part = ctext[-num_bits_end:]
key_end = []
for i in range(num_bits_end):
    key_end.append(binary_ptext_end[i] ^ ctext_end_part[i])
length, connection_polynomial = BM(key_end)
print(length)
print(connection_polynomial)

shift_register = key_end[:27][::-1]
print("Using initial state for the sequence generation: ", shift_register)
stream_sequence = [0] * num_bits_end
for index in range(num_bits_end):
    stream_sequence[index] = LFSR(connection_polynomial, shift_register)
print("Keystream corresponding to the given name: ", stream_sequence)
cipher_keystream = []
cipher_length = len(ctext)
for position in range(cipher_length):
    feedback_bit = shift_register[0] ^ shift_register[1] ^ shift_register[24] ^ shift_register[25]
    shift_register = shift_register[1:] + [feedback_bit]
    cipher_keystream.insert(0, shift_register[-1])
print("Keystream for the XOR operation derived: ", cipher_keystream)
plain_text = perform_xor(ctext, cipher_keystream)
print("Decoded text: ", bin2ASCII(plain_text))


