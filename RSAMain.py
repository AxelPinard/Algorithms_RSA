from re import L
import RSAalgorithmsClass
import random

"""
NOTES

n = pq ---- this is calculated in the generate_phi function
e = public key
d = Private key
"""

#Generate Keys
print("RSA keys have been generated.")
print("")
RSA = RSAalgorithmsClass.my_class()

#list to hold all of the encrypted messages
List_Of_Messages = []
List_Of_Sig = []

#This loop contains the User interface menu
while True:
    
    #list to hold ASCII and Encrypted message
    encryptedMessage = []

    print("Please select your user type:")
    print(      "1. A public user")
    print(      "2. The owner of the keys")
    print(      "3. Exit program")
    userSelection = int(input("Enter your choice: "))
    print("")

    #Public User Menu options
    while userSelection == 1:

        print("As a public user, what would you like to do?")
        print(      "1. Send an encrypted message")
        print(      "2. Authenticate a digitial signature")
        print(      "3. Exit")
        userSelection = int(input("Enter your choice: "))
        print("")
        
        #Sending an encrypted message
        if userSelection == 1:
            EncryptBool = True
            RSA.encrypt_decrypt(List_Of_Messages, EncryptBool)
        
        #Authenticate a digital signature
        if userSelection == 2:
            print("The following Signatures are available:")
            for x in range(len(List_Of_Sig)):
                print(str(x+1) + ". (length = " + str(len(List_Of_Sig[x])) + ")")
            userSelection = int(input("Enter your choice: "))
            print("")
            notEncryptedText = ""
            for x in List_Of_Sig[userSelection-1]:
                notEncryptedText += chr(RSA.fastExpo_rec(x, RSA.e,RSA.n))
            print("Signature is valid")
            print("")

        #Exit out of Public User Menu
        if userSelection == 3:
            userSelection = 0
            break

        #Reset UserSelection 
        userSelection = 1
            
    #Owner of the keys options
    while userSelection == 2:
        
        print("As the owner of the keys, what would you like to do?")
        print(      "1. Decrypt a received message")
        print(      "2. Digitally sign a message")
        print(      "3. Show the keys")
        print(      "4. Generating a new set of the keys")
        print(      "5.Exit")
        userSelection = int(input("Enter your choice: "))
        print("")

        #Decrypt a recieved message
        if userSelection == 1:
            EncryptBool = False
            List_Of_Messages = RSA.encrypt_decrypt(List_Of_Messages, EncryptBool)
        
        #Digitally sign a message
        if userSelection == 2:
            notEncryptedText = input("Enter a message: ")
            print("")
            notEncryptedText = notEncryptedText.upper()
        
            #loop to Sign the message and put in List of Signatures
            for x in notEncryptedText:
                encryptedMessage.append(RSA.fastExpo_rec(ord(x), RSA.d, RSA.n)) 

            List_Of_Sig.append(encryptedMessage)

            print("Message Signed and sent.")

        #Shop the keys
        if userSelection == 3:
            print("Public key: " + str(RSA.e))
            print("Private key: " + str(RSA.d))
            print("")

        #Generate new set of keys
        if userSelection == 4:
            RSA = RSAalgorithmsClass.my_class()
            print("New keys have been generated")
            print("")

        #Exit out of Owner of keys menu
        if userSelection == 5:
            userSelection = 0
            break

        #reset userSelection
        userSelection = 2

    if userSelection == 3:
        break
