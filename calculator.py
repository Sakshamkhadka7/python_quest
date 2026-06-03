def addition():
    value1=float(input("Enter the first number"))
    value2=float(input("Enter the second number"))
   
    return value1 + value2

def subtraction():
    value1=float(input("Enter the first number"))
    value2=float(input("Enter the second number"))
    
    return value1 - value2
   
def multiplication():
    value1=float(input("Enter the first number"))
    value2=float(input("Enter the second number"))
   
    return value1 * value2

def division():
    try :
        value1=float(input("Enter the first number"))
        value2=float(input("Enter the second number"))

        return value1/value2

    except ZeroDivisionError:
        print("You cannot divide by zero")

    except ValueError:
        print("Please enter valid number")

def calculator():
    print("Welcome to the calculator")
    print("1 Addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("e for exit")

    while True :
        choice=input("Choose an operation (1,2,3,4) 0r e for quit : ")
        if choice =='e':
            print("Exiting the calculator")
            break
        
        if choice=='1':
            print(f"The result of addition is :{addition()}" )
        elif choice=='2':
            print(f"The result of subtraction is : {subtraction()}")
        elif choice=='3': 
            print(f"The result of multiplication is : {multiplication()}")
        elif choice=='4':
            print(f"The result of division is : {division()}") 


calculator()   

   
