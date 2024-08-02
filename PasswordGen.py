# This Program Allows you to generate a Random Strong Password according to User's Specifications
# Length of the Password
# Special Characters 
# Numbers


# Importing Libraries
import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    #Calling the String Functions
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #print(letter,digits,special)
    # Creating a String which contains all the characters need for generating password upon given parameter of user
    characters = letter
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special

    pwd = ""
    meetchr= False
    has_number = False
    has_special = False


    # Here checking all the requriements need to assign No. and Special Charactes + assigning a random new character 
    while not meetchr or len(pwd) < min_length:
        new_chr = random.choice(characters)
        pwd+=new_chr

        if new_chr in digits:
            has_number = True
        elif new_chr in special:
            has_special = True
        meetchr = True
        if numbers:
            meetchr = has_number
        if special_characters :
            meetchr = meetchr and has_special

    return pwd

# Main
n=int(input("Enter the Lenght for the password to Generate :"))
num=input("Do you want to have No. in your password(y/n):")
if num == 'y' or num =='Y':
    num = True
elif num =='n' or num== 'N':
    num = False
else:
    num = True
sp=input("Do you want to have Special Characters in your password(y/n)")
if sp == 'y' or sp=='Y':
    sp = True
elif sp =='n' or sp== 'N':
    sp = False
else:
    sp = True
pas=generate_password(n,num,sp)
print(f"The Password Generated is : {pas}")