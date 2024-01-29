#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def decrypt_rsa(N, C, e):
    factors = factorize(N)
    if len(factors) != 2 or factors[0] * factors[1] != N:
        return "N cannot be factorized into two distinct primes."

    p, q = factors
    phi_N = (p - 1) * (q - 1)
    d = pow(e, -1, phi_N)
    M = pow(C, d, N)
    return M

N = 9244432371785620259
C = 655985469758642450
e = 2**16 + 1

decrypted_message = decrypt_rsa(N, C, e)

mx = decrypted_message.to_bytes((decrypted_message.bit_length() // 8 + 1 ), byteorder = 'big').decode('UTF-8')
print("Message is:", mx)


