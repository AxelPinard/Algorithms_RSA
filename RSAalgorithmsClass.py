import random

class my_class():
    """class"""
    ## list to store n
    n_List = []
    
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
    
    ## a necessary eviiiil
    def generate_n(self):
        n = self.n
        return n
    
    
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


    def encrypt_Message(self):
        notEncryptedText = input("Enter a message: ")
        print("")
        ## makes the message upperCase
        notEncryptedText = notEncryptedText.upper()
        encryptedMessage = []
        
        #loop to Encrypt the message and put into encryptedMessage list
        for x in notEncryptedText:
            encryptedMessage.append(self.fastExpo_rec(ord(x), self.e, self.n)) 
            
        print("Message encrypted and sent.")
        print("")
        
        return encryptedMessage
        
    
    
    
    ## DO NOT TOUCH THIS, IT IS FRAGILE
    def decrypt_Message(self, list_Of_Encrypted_Messages, privateKeyList, n_List):
        print("The following messages are available:")
        
        ## Prints what messages are available in the list
        for x in range(len(list_Of_Encrypted_Messages)):
            print(str(x + 1) + ". (length = " + str(len(list_Of_Encrypted_Messages[x])) + ")")
            
        userSelection = int(input("Enter your choice: "))
        print("")  
        
        decryptedMessage = ""
        ## loops through the encrypted message selected by the user, decrypts,
        ## and prints the message.
        for x in list_Of_Encrypted_Messages[userSelection - 1]:
            decryptedMessage += chr(int(self.fastExpo_rec(x, privateKeyList[userSelection - 1], n_List[userSelection - 1])))
            
        ## return the decrypted message as a string to be appended to the list 
        return decryptedMessage
        #######################################################################

    def sign_Message(self, signature):  ## Digitally sign or Authenticate
        ## private key owner creating signature to authenticate by public user
        encrypted_signature = []
        #loop to Encrypt the message and return the encrypted signature list
        for x in signature:
                encrypted_signature.append(self.fastExpo_rec(ord(x), self.d, self.n))
            
        print("Message signed and sent.")
        print("")
        return encrypted_signature
        
    
        #######################################################################
    def auth_Signature(self, list_Of_SigToCompare, list_Of_Encrypted_Signatures, list_Of_AuthKeys, list_Of_Sign_n):
        print("The following messages are available: ")
        ## loop to display what signatures are available for verification
        for x in range(len(list_Of_Encrypted_Signatures)):
            print(str(x + 1) + ". " + str(list_Of_SigToCompare[x]))
        userSelection = int(input("Enter your choice: "))
        print("")
        
        decryptedSignature = ""
        ## loop through the encrypted signature selected by the user and decrypts it
        ## IF YOU GENERATE NEW KEYS AS A PRIVATE USER, THEN TRY TO DECRYPT A NEW SIGNATURE AS A PUBLIC USER, THE PROGRAM CRASHES
        ## this is because of the value created from a new key not being a valid parameter inside of the chr function below.
        for x in list_Of_Encrypted_Signatures[userSelection - 1]:
            decryptedSignature += chr(int(self.fastExpo_rec(x, list_Of_AuthKeys[userSelection - 1], list_Of_Sign_n[userSelection - 1])))
        ## return the decrypted signature
        return decryptedSignature

    def __init__(self):
        """Initializes the object and assigns the private/public key"""
        self.phi = self.generate_phi()
        self.e = self.generate_public_key(self.phi)
        self.d = self.generate_private_key(self.e, self.phi)
        self.n = self.generate_n()
   