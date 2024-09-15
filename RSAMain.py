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
RSA = RSAalgorithmsClass.my_class()

#list to hold all of the encrypted messages
List_Of_Messages = []

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
    if userSelection == 1:
        print("As a public user, what would you like to do?")
        print(      "1. Send an encrypted message")
        print(      "2. Authenticate a digitial signature")
        print(      "3. Exit")
        userSelection = int(input("Enter your choice: "))
        print("")
        
        #Sending an encrypted message
        if userSelection == 1:
            notEncryptedText = input("Enter a message: ")
            notEncryptedText = notEncryptedText.upper()
        
            #loop to Encrypt the message and put in List of Messages
            for x in notEncryptedText:
                encryptedMessage.append(RSA.fastExpo_rec(ord(x), RSA.e, RSA.n)) 
            List_Of_Messages.append(encryptedMessage)

            print("Message encrypted and sent.")
    
    #Owner of the keys options
    if userSelection == 2:
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
            print("The following messages are available:")
            for x in range(len(List_Of_Messages)):
                print(str(x+1) + ". (length = " + str(len(List_Of_Messages[x])) + ")")
            userSelection = int(input("Enter your choice: "))
            notEncryptedText = ""
            for x in List_Of_Messages[userSelection-1]:
                notEncryptedText += chr(RSA.fastExpo_rec(x, RSA.d,RSA.n))
            print("Decrypted Message: " + notEncryptedText)
            print("")
