#!/usr/bin/env python
# coding: utf-8

# In[5]:


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


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

# Given values
values = [
    (2163549842134198432168413248765413213216846313201654681321666, 790561357610948121359486508174511392048190453149805781203471, 789213546531316846789795646513847987986321321489798756453122),
    (3213658549865135168979651321658479846132113478463213516854666, 789651315469879651321564984635213654984153213216584984653138, 798796513213549846121654984652134168796513216854984321354987),
    (5465132165884684652134189498513211231584651321849654897498222, 654652132165498465231321654946513216854984652132165849651312, 987965132135498749652131684984653216587986515149879613516844),
    (6285867509106222295001894542787657383846562979010156750642244, 798442746309714903987853299207137826650460450190001016593820, 263077027284763417836483408268884721142505761791336585685868)
]

def solve_congruence_all_solutions(n, a, b):
    gcd_a_n = gcd(a, n)
    if b % gcd_a_n != 0:
        return "No solution exists."
    a, b, n = a // gcd_a_n, b // gcd_a_n, n // gcd_a_n
    a_inv = modinv(a, n)
    x0 = (a_inv * b) % n
    solutions = [(x0 + i * n) % (n * gcd_a_n) for i in range(gcd_a_n)]
    return solutions

solutions = []
for n, a, b in values:
    solutions = solve_congruence_all_solutions(n, a, b)
    print(f"The solutions of {a}x ≡ {b} are: {solutions} \n\n")

