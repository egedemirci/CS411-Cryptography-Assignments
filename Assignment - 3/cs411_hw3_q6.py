#!/usr/bin/env python
# coding: utf-8

# In[6]:


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m

a1, b1, q1 = 2700926558, 967358719, 3736942861
a2, b2, q2 = 1759062776, 1106845162, 3105999989
a3, b3, q3 = 2333074535, 2468838480, 2681377229

r1 = (a1 * b1) % q1
r2 = (a2 * b2) % q2
r3 = (a3 * b3) % q3

Q = q1 * q2 * q3

n1, n2, n3 = Q // q1, Q // q2, Q // q3
m1 = modinv(n1, q1)
m2 = modinv(n2, q2)
m3 = modinv(n3, q3)

R = (r1 * m1 * n1 + r2 * m2 * n2 + r3 * m3 * n3) % Q

reconstructed_r1 = R % q1
reconstructed_r2 = R % q2
reconstructed_r3 = R % q3

print(r1, r2, r3, R, (reconstructed_r1, reconstructed_r2, reconstructed_r3))

