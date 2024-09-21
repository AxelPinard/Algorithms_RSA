import random

# Finds greatest common divisor (Euclid's algorithm)
def gcd(a=1, b=1):
    """Returns the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Finds the greatest common divisor and coefficients x and y
# (Euclid's Extended Algorithm)
def extended_gcd(a=1, b=1):
    """Returns the gcd(a,b) and x, y where a*x + b*y = gcd(a,b)."""
    # Base case
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y

# Checks if num is prime
def is_prime(num):
    """Checks if num is prime using while-loop to check divisibility."""
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Fermat Primality test
def fermat_prime():
    """Performs Fermat Primality Test."""
    k = 5  # number of iterations
    p = random.randint(1000, 9999) # Generate rand number b/w 1000 and 9999
    pseudo_prime = False

    while not pseudo_prime:
        for i in range(k):
            # Rand base
            j = random.randint(2, p - 1)
            if pow(j, p - 1, p) != 1:
                # Generate new number
                p = random.randint(1000, 9999)
                break
        else:
            pseudo_prime = True

        if is_prime(p):
            return p
        else:
            pseudo_prime = False

# Generates phi and n
def generate_phi():
    """Generates phi = (p-1) * (q-1) and n = p * q."""
    # Generate p and q
    p = fermat_prime()
    q = fermat_prime()
    # Calculate phi
    phi = (p - 1) * (q - 1)
    # Calculate n
    n = p * q
    return phi, n

# Generates public key
def generate_public_key(phi):
    """Generates public key e"""
    # Ensure phi is greater than 1, otherwise throw error
    if phi <= 1:
        raise ValueError("phi must be greater than 1!")
    
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e

# Generates private key
def generate_private_key(e, phi):
    """Generates private key d"""
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        raise ValueError(f"No multiplicative inverse for e={e} and phi={phi}!")
    
    d = x % phi
    return d

# Fast modular exponentiation
def fast_expo_rec(c, d, n):
    """Fast Modular Exponentiation Recursive Algorithm"""
    # Base case
    if d == 0:
        return 1 
    # If exponent is EVEN
    if d % 2 == 0:
        # Calculate result for 1/2 exponent
        t = fast_expo_rec(c, d // 2, n)
        # Square result then mod n
        result = (t * t) % n
        return result
    # If exponent is ODD
    else:
        # Calculate result for 1/2 exponent
        t = fast_expo_rec(c, d // 2, n)
        # Square result and multiply by c, then mod n
        result = (c * (t ** 2 % n)) % n
        return result

# Encryption
def encrypt_message(message, e, n):
    """Encrypts a message using the public key."""
    # Convert message to uppercase for uniformity
    message = message.upper()
    encrypted_message = []
     
    # Convert message to Unicode and generate encrypted values
    for x in message:
         encrypted_message.append(fast_expo_rec(ord(x), e, n)) 
         
    print("Message encrypted and sent.")
    print("")
    
    return encrypted_message

# Decryption
def decrypt_message(encrypted_message, d, n):
    """Decrypts a message using the private key."""
    decrypted_message = ''
    for char in encrypted_message:
        try:
            # Decrypt char using private key and n
            decrypted_char_value = fast_expo_rec(char, d, n)
            # Convert decrypted value to char
            decrypted_char = chr(decrypted_char_value)
            # Append char to message
            decrypted_message += decrypted_char
        # Throw an exception for invalid key
        except Exception as error:
            raise ValueError("\nDecryption failed! Invalid key.\n")
    return decrypted_message

# Digitally signs message
def sign_message(message, d, n):
    """Signs a message using the private key."""
    encrypted_signature = []
    for char in message:
        # Convert char to Unicode
        char_value = ord(char)
        # Encrypte value using private key and n
        encrypted_char = fast_expo_rec(char_value, d, n)
        # Append to signature
        encrypted_signature.append(encrypted_char)
    print("Message signed and sent.\n")
    return encrypted_signature

# Authenticate Digital Signature
def authenticate_signature(signature, encrypted_signature, e, n):
    """Authenticates the signature using the public key."""
    decrypted_signature = ''
    for char in encrypted_signature:
        # Decrypt Unicode value to char
        decrypted_char_value = fast_expo_rec(char, e, n)
        decrypted_char = chr(decrypted_char_value)
        # Append char to decrypted signature
        decrypted_signature += decrypted_char
    # Check if decrypted signature matches original
    if decrypted_signature == signature:
        is_authentic = True
    else:
        is_authentic = False
    return is_authentic

def main():
    """"Main menu: prompts users with menu options."""
    # Set RSA keys
    phi, n = generate_phi()
    e = generate_public_key(phi)
    d = generate_private_key(e, phi)
    print("RSA keys have been generated.\n")
    
    # Lists containing encrypted messages and signatures
    list_of_encrypted_messages = []
    list_of_encrypted_signatures = []
    list_of_signatures = []
    
    # User Interface Menu
    while True:
        print("Please select your user type:")
        print("    1. A public user")
        print("    2. The owner of the keys")
        print("    3. Exit program\n")
        
        user_selection = int(input("Enter your choice: "))
        print("")
        
        # Execute code based on user input
        
        # Public user
        if user_selection == 1: 
            while True:
                # Prompt user for menu option
                print("As a public user, what would you like to do?")
                print("    1. Send an encrypted message")
                print("    2. Authenticate a digital signature")
                print("    3. Back to menu\n")
                
                user_selection = int(input("Enter your choice: "))
                print("")
                
                # Encrypt Message
                if user_selection == 1:
                    message = input("Enter a message: ")
                    encrypted_message = encrypt_message(message, e, n)
                    list_of_encrypted_messages.append(encrypted_message)
                
                # Authenticate Signature
                elif user_selection == 2:
                    if list_of_encrypted_signatures:
                        # List each signature (1. sig1, 2. sig2)
                        for i, signature in enumerate(list_of_signatures):
                            print(f"{i + 1}. {signature}")
                        user_selection = int(input("Enter your choice: "))
                        try:
                            
                            is_authentic = authenticate_signature(
                                list_of_signatures[user_selection - 1],
                                list_of_encrypted_signatures[user_selection - 1], 
                                e, n)
                            if is_authentic:
                                print("Signature is valid.\n")
                            else:
                                print("ERROR: Signature is invalid!\n")
                        # Throw an exception for invalid key
                        except ValueError as error:
                            print("\nAuthentication failed! Invalid keys or signature.\n")
                    else:
                        print("No signatures found.\n")
                
                # Exit public user menu
                elif user_selection == 3:
                    break
                
        # Owner of the keys
        elif user_selection == 2:  
            while True:
                print("As the owner of the keys, what would you like to do?")
                print("    1. Decrypt a received message")
                print("    2. Digitally sign a message")
                print("    3. Show the keys")
                print("    4. Generate a new set of keys")
                print("    5. Back to menu\n")
                
                user_selection = int(input("Enter your choice: "))
                print("")
                
                # Decrypt message
                if user_selection == 1:
                    for i, msg in enumerate(list_of_encrypted_messages):
                        print(f"{i + 1}. (length = {len(msg)})")
                    user_selection = int(input("Enter the number of the message to decrypt: "))
                    try:
                        decrypted_message = decrypt_message(list_of_encrypted_messages[user_selection - 1], d, n)
                        print(f"Decrypted Message: {decrypted_message}\n")
                    # Print exception message if keys are invalid
                    except ValueError as error:
                        print(error)
                
                # Sign message
                elif user_selection == 2:
                    signature = input("Enter a message to sign: ")
                    encrypted_signature = sign_message(signature, d, n)
                    list_of_signatures.append(signature)
                    list_of_encrypted_signatures.append(encrypted_signature)
                
                # Show keys
                elif user_selection == 3:
                    print(f"Public key: {e}")
                    print(f"Private key: {d}\n")
                
                # Generate new keys
                elif user_selection == 4:
                    phi, n = generate_phi()
                    e = generate_public_key(phi)
                    d = generate_private_key(e, phi)
                    print("New keys have been generated.\n")
                
                # Navigate back to menu
                elif user_selection == 5:
                    break
                
        # Exit program
        elif user_selection == 3:
            break
main()