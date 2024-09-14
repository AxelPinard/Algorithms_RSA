import random

class my_class():
    """class"""

    def gcd(self,a=1, b=1):
        """Returns the greatest common divisor of a and b.(Euclid's algorithm)"""
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)
    
    def extended_gcd(self, a=1, b=1):
        """Returns the gcd(a,b) and x, y where a*x + b*y = gcd(a,b).(Euclid's Extended Algorithm)"""
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = self.extended_gcd(b, a%b)
        x = y1
        y = x1 - (a//b) * y1
        return gcd, x, y
    
    def is_prime(self,num):
        """Checks if num is prime using while-loop to check divisibility."""
        if num < 2:
            return False
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def generate_prime(self,low = 1000, high = 9999):
        """Generates a random prime number between low and high values."""
        while True:
            num = random.randint(low, high)
            if self.is_prime(num):
                return num

    def generate_phi(self):
        """Generates phi = (p-1) * (q-1)."""
        p = self.generate_prime()
        q = self.generate_prime()
        phi = (p-1) * (q-1)
        return phi

    def generate_public_key(self,phi):
        """Generates public key e"""
        if phi <= 1:
            raise ValueError("phi must be greater than 1!")
    
        while True:
            e = random.randint(2, phi-1)
            if self.gcd(e, phi) == 1:
                return e
        
    def generate_private_key(self,e, phi):
        """Generates private key d"""
        gcd, x, y = self.extended_gcd(e, phi)
        if gcd != 1:
            raise ValueError(f"No multiplicative inverse for e={e} and phi={phi}!")
        d = x % phi
        return d

    def __init__(self):
        self.phi = self.generate_phi()
        self.e = self.generate_public_key(self.phi)
        self.d = self.generate_private_key(self.e, self.phi)
   




