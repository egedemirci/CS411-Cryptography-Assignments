#!/usr/bin/env python
# coding: utf-8

# In[2]:


# use "pip install sympy" if pyprimes is not installed
# use "pip install pycryptodome" if pycryptodome is not installed
import random
import sympy
import warnings
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHAKE128

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = a+m
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def random_prime(bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        p = random.randrange(2**(bitsize-1), 2**bitsize-1)
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def large_DL_Prime(q, bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        k = random.randrange(2**(bitsize-1), 2**bitsize-1)
        p = k*q+1
        chck = sympy.isprime(p)
    warnings.simplefilter('default')    
    return p

def Param_Generator(qsize, psize):
    q = random_prime(qsize)
    p = large_DL_Prime(q, psize-qsize)
    tmp = (p-1)//q
    g = 1
    while g == 1:
        alpha = random.randrange(1, p)
        g = pow(alpha, tmp, p)
    return q, p, g

# Generating private-public key pair
def Key_Gen(q, p, g):
    s = random.randint(1, q) # private key
    h = pow(g, s, p)         # public key
    return s, h

# Signature generation
def Sig_Gen(message, a, k, q, p, g):
    shake = SHAKE128.new(message)
    h = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
    r = pow(g, k, p)%q
    s = (modinv(k, q)*(h+a*r))%q
    return r, s

# Signature verification
def Sig_Ver(message, r, s, beta, q, p, g):
    shake = SHAKE128.new(message)
    h = int.from_bytes(shake.read(q.bit_length()//8), byteorder='big')
    u1 = (modinv(s, q)*h)%q
    u2 = (modinv(s, q)*r)%q
    v1 = (pow(g, u1, p)*pow(beta, u2, p)%p)%q

    if v1 == r:
        return True
    else:
        return False


q = 18055003138821854609936213355788036599433881018536150254303463583193
p = 17695224245226022262215550436146815259393962370271749288321196346958913355063757122216400038699125897137338245645654623180907445775397476914326454182331200843039828753210051963838673399537750764519381124074022003533048362953579747694997421932628050174768037008419023891955638333683910783296320068313502467953549845629364328685168055331330378439460107262672207911384029916731040428600795952248385683448339051326373879623024586381484917048530867998300839452185045027743182645996068845915287513974737094311071485279830178802332884322953485032954055698263286829168380561154757985319675247125962424242568733265799534941009
g = 4789073941777232663925946116548512236454007195930716545844255515671921902088454647562920559586402554819251607533026386568443177012595965432651516494873094284671880587043080168709792729580864399522070440013588701427100770785527321717784068531253489015313171638446034805847845720567691412760307220603939165634874434595948570583948951567783902643539632274510317008676675644324152107083325484901562104857644621121348409411557653041824973063215599539520882871449851513387270613400464314879652836352363637833225350963794362275261801894957372518031031893668151623517523940210995342229628030114190419396207343174070379971035
beta = 1831408160533218510686903726138665932536518466931856989835941853268730468186911958415037229987343935227988816813155415974234360530276380966386586121747340348158553225363319918657949382937198455018294836381584550181800201868806694527418279797492758151769276850910944244395645572497766748854242598561659704665374023326770662512666613356092618904914953512155804252127648818534285831773370510453137952688543495010103660892413395901461238209725480737625047159275781922088076720717434062444236969393756880954396658965471745598003472511293882525516878617801436300794663357187223445935638034452125753926695866508095018852433


message1, r_1, s_1 = b'The grass is greener where you water it.', 16472915699323317294511590995572362079752105364898027834238409547851, 959205426763570175260878135902895476834517438518783120550400260096
message2, r_2, s_2 = b'Sometimes you win, sometimes you learn.', 14333708891393318283285930560430357966366571869986693261749924458661, 9968837339052130339793911929029326353764385041005751577854495398266



def compute_hash(message, q):
    shake = SHAKE128.new(message)
    return int.from_bytes(shake.read(q.bit_length() // 8), byteorder='big')

# Calculate the inverse of s_1 and s_2 modulo q
s1_inv = modinv(s_1, q)
s2_inv = modinv(s_2, q)

# Compute the hashes of the messages
h1 = compute_hash(message1, q)
h2 = compute_hash(message2, q)

# Calculate the components for the equation to solve for 'a'
# Multiplying the inverse of s1 with h1 and the inverse of s2 with h2
h1_s1_inv = (s1_inv * h1) % q
h2_s2_inv = (s2_inv * h2) % q

# Multiplying the inverse of s1 with r1 and the inverse of s2 with r2
r1_s1_inv = (s1_inv * r_1) % q
r2_s2_inv = (s2_inv * r_2) % q

# Apply the relationship between k_1 and k_2 (i.e., k_2 = 3k_1 mod q)
# Given the DSA signature equations for both messages:
# s_1 = (k_1^{-1}(H(m_1) + a * r_1)) mod q
# s_2 = (k_2^{-1}(H(m_2) + a * r_2)) mod q
# We can rearrange these to express k_1 and k_2:
# k_1 = s_1^{-1}(H(m_1) + a * r_1) mod q
# k_2 = s_2^{-1}(H(m_2) + a * r_2) mod q
# Substituting k_2 with 3k_1 mod q in the s_2 equation gives us:
# 3 * s_1^{-1} * (H(m_1) + a * r_1) = s_2^{-1} * (H(m_2) + a * r_2) mod q
# Multiplying both sides by s_1 and s_2 to isolate terms involving 'a', we get:
# 3 * s_2 * (H(m_1) + a * r_1) = s_1 * (H(m_2) + a * r_2) mod q
# Rearranging to factor out 'a':
# a * (3 * s_2 * r_1 - s_1 * r_2) = s_1 * H(m_2) - 3 * s_2 * H(m_1) mod q
# Now we can solve for 'a' by isolating it on one side:
# a = (s_1 * H(m_2) - 3 * s_2 * H(m_1)) / (3 * s_2 * r_1 - s_1 * r_2) mod q

numerator = ((s_1 * h2) - (3 * s_2 * h1)) % q
denominator = ((3 * s_2 * r_1) - (s_1 * r_2)) % q

# The final step is to solve for 'a' using these components:
a = (numerator * modinv(denominator, q)) % q

print("The secret key 'a' is:", a)



# In[ ]:




