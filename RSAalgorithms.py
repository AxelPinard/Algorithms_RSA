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