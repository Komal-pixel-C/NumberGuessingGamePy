import random as rd

def Guess1(start,end):
    print("Random Number guessing using For Loop and LIST creation method")
    trial = 3
    cntr = 1
    l =[]
    for i in range(start, end):
        l.append(i)
    
    randPick = rd.choice(l)

    
    for i in range(1,trial+1):
        try1 = int(input((f'Guess the no {i}st Try:')))
        cntr += 1
        if try1 == randPick:
            print(f"You guess correct")
            exit()
        elif i!= trial:
            print(f"Wrong Guess !! You can try Again to Guess:) ")
        else:
            print(f"You r end of Guess - Correct No was {randPick}")
    



#def Guess2(start,end):
    

# Input Validation
a= int(input("select 1st range value: "))
b= int(input("Select 2nd range value:"))

# try-catch Block

try:
    if(a>=b):
        print(f'Invalid range. The first value should be less than the second value.')
        exit()
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()



print(Guess1(a,b))

