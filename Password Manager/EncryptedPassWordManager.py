# This is a Passcode / Password managing program which only shows the correct password to the user who is the
# Actual owner -> otherwise show the encrypted format | helps in providing abstraction on different levels

#                                               Password Manager Using CryptoGraphy(Encrypted form)
# Can also be done using MySQL or CSV for larger data + can also Make level of extraction

# importing the library which will help us to convert the Normal text to Cryptic(Encoded) text
from cryptography.fernet import Fernet

# To be Runned Only Once -> Just to Create a Key 
'''
def write_key():
    key = Fernet.generate_key()
    with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/PassMananger/key.key","wb") as keyfile : # wb -> write in binary
        keyfile.write(key)
'''

def load_key():
    
    file =open("/Users/kartikeysharma/Desktop/Hanuman/Projects/PassMananger/key.key","rb") # rb -> read binary
    key = file.read()
    file.close()
    return key


# encode takes the string and encode it into bytes / or binary form 
mspass = input("Enter the Master Password :")
Okey=load_key() + "kk".encode()
Mskey=load_key() + mspass.encode()

fer=Fernet(Okey)

# So what we are gonna do here is Create a key which is associated to a Master password so the person having the master password
# can only view or see the data in the file in decrypted format else if will be seen in encrypted format

# key + password + text to encrypt = random text      : Encoding 
# random + key + password -> give the text to encrypt : Decoding 



# Function is Excutable reusable block of code + also helps to organize the code better
def view():
    with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/PassMananger/Credentials.txt","r") as rCred:
        for re in rCred.readlines():
            data = re.rstrip()
            usn,paswd= data.split("|")
            print(f"User Name :{usn} , Password :{fer.decrypt(paswd.encode()).decode()}")

def view2():
    with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/PassMananger/Credentials.txt","r") as rCred:
        for re in rCred.readlines():
            data = re.rstrip()
            usn,paswd= data.split("|")
            print(f"User Name :{usn} , Password :{paswd}")

def add():
    name = input("User Name :")
    pswd = input("Password  :")

    # Using "with" the file will be closed automatically as soon as you comes out of the loop
    # while if you open the file without "with" you have to manually close the file
    
    with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/PassMananger/Credentials.txt","a") as Cred : 
        Cred.write(f"{name} | {fer.encrypt(pswd.encode()).decode()}"+"\n")        


# Adding New Password or Viewing the Existing Password 
while True :
    print('''
    1. View
    2. Add New Credentials 
    3. Quit
    ''')
    mode = int(input("Enter the Index no. to which you want to proceed From the above choice :"))
    print()
    if mode == 1:
        if Okey == Mskey:
            view()
        else:
            view2()
    elif mode == 2:
        add()
    elif mode == 3:
        print("Thank You!!!")
        break
    else:
        print("Pls choose the Correct Option")