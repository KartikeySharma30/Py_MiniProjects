#                                                    '''Computer Quiz Game'''
print("Welcome to the Computer Quiz Game!!")
playing = input("Do you want to Play? ").lower()
if playing != "yes":
    quit()

print("yo")
score=0

answer = input("What does CPU stands for :").lower()
if(answer=="central processing unit"):
    print("Correct!!")
    score+=1
else:
    print("Incorrect")


answer = input("What does GPU stands for :").lower()
if(answer=="graphic processing unit"):
    print("Correct!!")
    score+=1
else:
    print("Incorrect")

answer = input("What does RAM stands for :").lower()
if(answer=="random access memory"):
    print("Correct!!")
    score+=1
else:
    print("Incorrect")

print(f"You got {score} questions correct")
print(f"You got {(score/3)*100} %")
