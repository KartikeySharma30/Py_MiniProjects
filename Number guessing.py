import random

n=input("Enter a No. :")
if n.isdigit():
    n=int(n)
    if(n<=0):
        print("Please Enter a No. greater than 0 :")
        quit()
        
else:
    print("Please Enter a Valid Digit!!")
    quit()


# randrange doesnt include the upper bound but randint includes
rn=random.randint(0,n)
print(rn)
gus=0
while True:
    gus+=1
    x=int(input("Enter your Guess :"))
    if(rn==x):
        print("Prefect! \nYou Guessed it :)")
        break
    elif(x>rn):
        print("Enter a No. Smaller")       
    else:
        print("Enter a No. Greater")
print(f"You Guessed in : {gus} Gusses")

