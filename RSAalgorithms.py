import random

def gcd(a=1, b=1):
    """
    Returns the greatest common divisor of a and b.
    (Euclid's algorithm)
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def extended_gcd(a=1, b=1):
    """
    Returns the gcd(a,b) and x, y where a*x + b*y = gcd(a,b).
    (Euclid's Extended Algorithm)
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return gcd, x, y

def is_prime(num):
    """Checks if num is prime using while-loop to check divisibility."""
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def generate_prime(low=1000, high=9999):
    """Generates a random prime number between low and high values."""
    while True:
        num = random.randint(low, high)
        if is_prime(num):
            return num
        
def generate_phi():
    """Generates phi = (p-1) * (q-1)."""
    p = generate_prime()
    q = generate_prime()
    phi = (p-1) * (q-1)
    return phi
    

def generate_public_key(phi):
    """Generates public key e"""
    if phi <= 1:
        raise ValueError("phi must be greater than 1!")
    
    while True:
        e = random.randint(2, phi-1)
        if gcd(e, phi) == 1:
            return e
        
def generate_private_key(e, phi):
    """Generates private key d"""
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"No multiplicative inverse for e={e} and phi={phi}!")
    d = x % phi
    return d

def generate_keys():
    """Generates both public and private keys."""
    phi = generate_phi()
    e = generate_public_key(phi)
    d = generate_private_key(e, phi)
    
## below this line is Jon --- 

def fastExpo_rec (c, d, n):
    """Fast Modular Exponentiation Recursive Algorithm """
    if d == 0:
        return 1 
    if d%2 == 0:
        t = fastExpo_rec(c, d//2, n)
        return (t * t) % n 
    else:
        t = fastExpo_rec(c, d//2, n)
        return c * (t**2%n) % n
    

def fermatPrime():
    p = random.randomint(1000, 9999)    ## using arbitrary numbers here
    pseudo_prime = False
    while not pseudo_prime:
        for i in range(k):              ## HOW DO WE DETERMINE K? Slides say constant integer
            j = random.randint(2, p)
            if pow(j, p - 1, p) > 1:
                p = random.randint(1000, 9999)
                break 
        pseudo_prime = True
    return p 

"""
FOR RSA KEY GENERATION

Generate two large pseudo primes p and q utilitizing the Fermat's tests algorithm
Test if p and q are prime 

Yes? ----> Find an e relative prime to (p - 1)(q - 1) utilitizing Euclids gcd algorithm
Then find the multiplicative inverse of e in Z(p - 1)(q - 1) utilizing Extended Euclid 
Output: n = pq, e and d

No? ----> back to Fermat's tests and generate more prime numbers


AVAILABLE TO PUBLIC

Encryption***
Input: message M
Public Key (n, e)
------>
Encrypt: C = M^e mod n utilizing fast modular exponentiation algorithm
in order to get the output, C

LIMITED TO PRIVATE ACCESS

Decryption***
Input: C 
Private key (n, d)
------>
Decrypt: M = C&d mod n utilizing fast modular exponentiation algorithm
in order to get the output, M
"""



























  
    
    