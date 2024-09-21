from re import L
import RSAalgorithmsClass
import random

"""
NOTES

n = pq ---- this is calculated in the generate_phi function
e = public key
d = Private key

OLD ENCRYPTION FOR LOOP

for x in notEncryptedText:
    ASCIIMessage.append(ord(x))
        print(x)
    for x in ASCIIMessage:
        encryptedMessage.append(RSA.fastExpo_rec(x, RSA.e, n)) ## message is encrypted and stored here
        print(encryptedMessage)

OLD DECRYPTION FOR LOOP

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

"""

## lists to hold all of our relevant data throughout the program's runtime

## holds all of the decrypted messages created when running the program. useful for debugging.
list_Of_Decrypted_Messages = []

list_Of_Encrypted_Messages = []

list_Of_Encrypt_Keys = []

list_Of_Decrypt_Keys = []

list_Of_n = []

list_Of_Sign_n = []

list_Of_Encrypted_Signatures = []

list_Of_Decrypted_Signatures = []

list_Of_SigToCompare = []

list_Of_AuthKeys = []

list_Of_SignKeys = []



signature = ""
#Generate Keys
## ***IMPORTANT*** initialize the RSA class object to access class methods and generate
## keys. The private user can do this again through the menu. 
RSA = RSAalgorithmsClass.my_class() 
print("RSA keys have been generated.")
print("")

#This loop contains the User interface menu
while True:
    
    #list to hold ASCII and Encrypted message
    encryptedMessage = []

    print("Please select your user type:")
    print(      "1. A public user")
    print(      "2. The owner of the keys")
    print(      "3. Exit program")
    print("")
    userSelection = int(input("Enter your choice: "))
    print("")

    #PUBLIC USER OPTIONS ######################################################
    match userSelection:
        case 1:
            while userSelection != 3:
                print("As a public user, what would you like to do?")
                print(      "1. Send an encrypted message")
                print(      "2. Authenticate a digital signature")
                print(      "3. Exit")
                print("")
                userSelection = int(input("Enter your choice: "))
                print("")
                
                ## ENCRYPTION HAPPENS HERE
                #Sending an encrypted message
                if userSelection == 1:
                    ## encryption function occurs here
                    encryptedMessage = RSA.encrypt_Message()
                    ## store the now encrypted message into the list of encrypted
                    ## messages so it can be accessed later. This is because we don't need 
                    ## to store the keys until they are actually used.
                    list_Of_Encrypted_Messages.append(encryptedMessage)
                    ## store the keys so that the correct keys get accessed when decrypting
                    list_Of_Encrypt_Keys.append(RSA.e)
                    list_Of_Decrypt_Keys.append(RSA.d)
                    ## do the same thing with n
                    list_Of_n.append(RSA.n)
                
                ##Authenticate a digital signature
                if userSelection == 2:
                    if (len(list_Of_Encrypted_Signatures) == int(0)):
                        print("There are no signatures to authenticate.")
                        print("")
                    else:
                        decryptedSignature = RSA.auth_Signature(list_Of_SigToCompare, list_Of_Encrypted_Signatures, list_Of_AuthKeys, list_Of_Sign_n)
                        list_Of_Decrypted_Signatures.append(decryptedSignature)
                        
                        if ((signature.upper()) == (list_Of_Decrypted_Signatures[-1].upper())):
                            print("Signature is valid.")
                            print("")
                        else:
                            print("Error validating signature. Key no longer available.")
                            print("")
                
                
        ##PRIVATE USER OPTIONS ################################################
        case 2:
            while userSelection != 5:
                print("As the owner of the keys, what would you like to do?")
                print(      "1. Decrypt a received message")
                print(      "2. Digitally sign a message")
                print(      "3. Show the keys")
                print(      "4. Generating a new set of the keys")
                print(      "5.Exit")
                print("")
                userSelection = int(input("Enter your choice: "))
                print("")
        
                #Decrypt a recieved message
                if userSelection == 1:
                    decryptedMessage = RSA.decrypt_Message(list_Of_Encrypted_Messages, list_Of_Decrypt_Keys, list_Of_n)
                    list_Of_Decrypted_Messages.append(decryptedMessage)
                    print("Decrypted Message: " + decryptedMessage)
                    print("")
                    
                
                #Digitally sign a message
                if userSelection == 2:
                    signature = input("Enter a message: ")
                    print("Message signed and sent.")
                    print("")
                    ## first store the original signature so once it is encrypted and decrypted,
                    ## we can compare the decrypted signature by the public user to the original
                    ## input
                    list_Of_SigToCompare.append(signature)
                    ## creates encrypted signature and appends it to list of signatures
                    list_Of_Encrypted_Signatures.append(RSA.sign_Message(signature))
                    ## store the keys so that the correct keys get accessed when decrypting
                    list_Of_SignKeys.append(RSA.d)
                    list_Of_AuthKeys.append(RSA.e)
                    ## do the same thing with n
                    list_Of_Sign_n.append(RSA.n)
                        
                #Show the keys
                if userSelection == 3:
                    print("Public key: " + str(RSA.e))
                    print("Private key: " + str(RSA.d))
                    print("")
        
                #Generate new set of keys
                if userSelection == 4:
                    RSA = RSAalgorithmsClass.my_class()
                    print("New keys have been generated")
                    print("")
                    ##store the encryption key
                    list_Of_Encrypt_Keys.append(RSA.e)
                    ##store the decryption key
                    list_Of_Decrypt_Keys.append(RSA.d)
                    ##store n
                    list_Of_n.append(RSA.n)
                    
        #######################################################################
        #Break out of program
        case 3:
            break
