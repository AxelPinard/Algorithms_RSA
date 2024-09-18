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
        """Returns the gcd(a,b) and x, y where a*x + b*y = gcd(a,b). (Euclid's Extended Algorithm)"""
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

    def fermatPrime(self):
        """Performs Fermat Primality Test."""
        k = 5  
        p = random.randint(1000, 9999)
        pseudo_prime = False
        
        while not pseudo_prime:
            for i in range(k):
                j = random.randint(2, p - 1)
                if pow(j, p - 1, p) != 1:
                    p = random.randint(1000, 9999)
                    break 
            else:
                pseudo_prime = True
                
            if self.is_prime(p):
                return p
            else:
                pseudo_prime = False

    def generate_phi(self):
        """Generates phi = (p-1) * (q-1)."""
        p = self.fermatPrime()
        q = self.fermatPrime()
        phi = (p-1) * (q-1)
        self.n = p * q
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

    def fastExpo_rec (self, c, d, n):
        """Fast Modular Exponentiation Recursive Algorithm """
        if d == 0:
            return 1 
        if d%2 == 0:
            t = self.fastExpo_rec(c, d//2, n)
            return (t * t) % n 
        else:
            t = self.fastExpo_rec(c, d//2, n)
            return c * (t**2%n) % n

    def encrypt_decrypt(self,List_Of_Messages, E_Or_D):
        if E_Or_D == True:
            notEncryptedText = input("Enter a message: ")
            print("")
            notEncryptedText = notEncryptedText.upper()
            encryptedMessage = []
            #loop to Encrypt the message and put in List of Messages
            for x in notEncryptedText:
                encryptedMessage.append(self.fastExpo_rec(ord(x), self.e, self.n)) 

            List_Of_Messages.append(encryptedMessage)

            print("Message encrypted and sent.")


       
        if E_Or_D == False:
            print("The following messages are available:")
            for x in range(len(List_Of_Messages)):
                print(str(x+1) + ". (length = " + str(len(List_Of_Messages[x])) + ")")
            userSelection = int(input("Enter your choice: "))
            print("")
            notEncryptedText = ""
            for x in List_Of_Messages[userSelection-1]:
                notEncryptedText += chr(self.fastExpo_rec(x, self.d,self.n))
            print("Message: " + notEncryptedText)
            print("")
            List_Of_Messages.pop(userSelection-1)

        return List_Of_Messages

    def Signature(self, List_Of_Sig, S_Or_A):

        if S_Or_A == True:
            print("The following Signatures are available:")
            for x in range(len(List_Of_Sig)):
                print(str(x+1) + ". (length = " + str(len(List_Of_Sig[x])) + ")")
            userSelection = int(input("Enter your choice: "))
            print("")
            notEncryptedText = ""
            for x in List_Of_Sig[userSelection-1]:
                notEncryptedText += chr(self.fastExpo_rec(x, self.e,self.n))
            print("Signature is valid")
            print("")

        if S_Or_A == False:
            notEncryptedText = input("Enter a message: ")
            print("")
            notEncryptedText = notEncryptedText.upper()
            encryptedMessage = []
            #loop to Sign the message and put in List of Signatures
            for x in notEncryptedText:
                encryptedMessage.append(self.fastExpo_rec(ord(x), self.d, self.n)) 

            List_Of_Sig.append(encryptedMessage)

            print("Message Signed and sent.")

        return List_Of_Sig

    def __init__(self):
        """Initializes the object and assigns the private/public key"""
        self.phi = self.generate_phi()
        self.e = self.generate_public_key(self.phi)
        self.d = self.generate_private_key(self.e, self.phi)
   