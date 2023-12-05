num1 = float(input("Enter the floting number 1 :  "))
num2 = float(input("Enter the floting number 2 :  "))

def floating ():
    # num1 = float(int(input("Enter the floting number 1 :  ")))
    # num2 = float(int(input("Enter the floting number 2 :  ")))
    if  type(num1) is float and type(num2) is float :
        # Addition
        add = num1 + num2
        print("==== Printing the Addition of " , num1, "and", num2)
        print(add)
        # Substraction
        sub = num1 - num2
        print("==== Printing the substraction of ", num1, "and", num2)
        print(sub)
        # Division
        Div = num1 // num2
        print("==== Printing the Divison of ", num1, "and", num2)
        print(Div)
        # multi
        mul= num1 // num2
        print("==== Printing the Multiplication of ", num1, "and", num2)
        print(mul)
    else:
        print("Please enter floating number")

floating()