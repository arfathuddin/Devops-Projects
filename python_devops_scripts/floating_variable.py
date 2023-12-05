# num1 = float(int(input("Enter the floting number 1 :  ")))
# num2 = float(int(input("Enter the floting number 2 :  ")))

# def floating ():
#     num1 = float(int(input("Enter the floting number 1 :  ")))
#     num2 = float(int(input("Enter the floting number 2 :  ")))
#     if  num1 and num2 is float :
#         # Addition
#         add = num1 + num2
#         print("==== Printing the Addition of " + num1 and num2)
#         print(add)
#         # Substraction
#         sub = num1 - num2
#         print("==== Printing the substraction of " + num1 and num2)
#         print(sub)
#         # Division
#         Div = num1 // num2
#         print("==== Printing the Divison of " + num1 and num2)
#         print(Div)
#         # multi
#         mul= num1 // num2
#         print("==== Printing the Multiplication of " + num1 and num2)
#         print(mul)
#     else:
#         print("Please enter floating number")

# floating()


# The below is the correction form of above code by chatGPT
def floating():
    try:
        num1 = float(input("Enter the floating number 1: "))
        num2 = float(input("Enter the floating number 2: "))
        
        # Addition
        add = num1 + num2
        print("==== Printing the Addition of", num1, "and", num2)
        print(add)
        
        # Subtraction
        sub = num1 - num2
        print("==== Printing the Subtraction of", num1, "and", num2)
        print(sub)
        
        # Division
        div = num1 / num2  # Use '/' for floating-point division
        print("==== Printing the Division of", num1, "and", num2)
        print(div)
        
        # Multiplication
        mul = num1 * num2  # Use '*' for multiplication
        print("==== Printing the Multiplication of", num1, "and", num2)
        print(mul)
    
    except ValueError:
        print("Please enter valid floating numbers")

floating()
