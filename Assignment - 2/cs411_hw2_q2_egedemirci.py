#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import requests

API_URL = 'http://harpoon1.sabanciuniv.edu:9999/'
my_id = 28287

def getQ2():
  endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    e, cipher = res['e'], res['cipher']
    return e, cipher
  else:  print(response.json())

def checkQ2(ptext):  #check your answer for Question 2
  response = requests.put('{}/{}'.format(API_URL, "checkQ2"), json = {"ID": my_id, "msg":ptext})
  print(response.json())

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y



e,c = getQ2()
p_value = 163812632438116402334651955238877888051471698595800699322979615035703105353498598900017754479082745390305183480326386193928762023006697325502630355995540302095536983747674239699082775937971908945314983176639634719523082664655125286220339981282043117576435108592265744474672826334454420325847233209118053745479

q_value = 167991311406281829893277907517380926743297770437237817698088843729837413680407121035993724942424328049100226903066919418963576739130754375674323262394889417412537943169688299724092631996519692955388293697048331540030669504591419100438660952486903606581569836090930608369486871356825028654569386086674053846173

n_value = p_value * q_value
phi_n_value = (p_value - 1) * (q_value - 1)
d_value = modinv(e, phi_n_value)
decrypted_message = pow(c, d_value, n_value)
decrypted_text = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big').decode('UTF-8')
print(decrypted_text)
checkQ2(decrypted_text)

