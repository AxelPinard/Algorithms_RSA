## functions are defined in RSAAlgorithms.py file
import RSAalgorithmsClass
import random

"""
NOTES

public key(n, e)
n = pq ---- this is calculated in the generate_phi function
e = public key

"""
RSA = RSAalgorithmsClass.my_class()     ## define RSA object to use the RSAalgorithmsClass functions
n = RSA.n                               ## this assigns n

ASCIIMessage = []
encryptedMessage = []

## FIRST MENU 

print("RSA keys have been generated.")
print("Please select your user type:")
print(      "1. A public user")
print(      "2. The owner of the keys")
print(      "3. Exit program")
userSelection = int(input("Enter your choice: "))

if userSelection == 1:
    print("As a public user, what would you like to do?")
    print(      "1. Send an encrypted message")
    print(      "2. Authenticate a digitial signature")
    print(      "3. Exit")
    userSelection = int(input("Enter your choice: "))
    
    if userSelection == 1:
        notEncryptedText = input("Enter a message: ")
        notEncryptedText = notEncryptedText.upper()
        
        for x in notEncryptedText:
            ASCIIMessage.append(ord(x))
            print(x)
        for x in ASCIIMessage:
            encryptedMessage.append(RSA.fastExpo_rec(x, RSA.e, n)) ## message is encrypted and stored here
            print(encryptedMessage)
        
        print("Message encrypted and sent.")