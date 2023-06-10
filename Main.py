def Addition(x, y):
    print(x+y)


def Subtraction(x, y):
    print(x-y)


def Multiplication(x, y):
    print(x*y)


def Division(x, y):
    print(x/y)

running = True 
while(running):
    print("Welcome to Amby's Spakulator")
    print()
    x = float(input("Please gently type the first number: "))    
    y = float(input("Please gently type the second number: "))
    operation = input("Please select operation(A-ddition, S-ubtraction, M-ultiplication, D-ivision): ").strip().upper()

    if(operation == "A"):
        Addition(x,y)
        running = False

    elif(operation == "S"):
        Subtraction(x,y)
        running = False
    
    elif(operation == "M"):
        Multiplication(x,y)
        running = False

    elif(operation == "D"):
        Division(x,y)
        running = False
        
    else:
        print("Not a valid statement")
    


