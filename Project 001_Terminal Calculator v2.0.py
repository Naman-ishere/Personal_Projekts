def addition(a, b):
    return a + b 

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

while True:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
 
    print("Please select an operation from the following:")
    print("1. Addition (Type 1)")
    print("2. Subtraction (Type 2)")
    print("3. Division (Type 3)")
    print("4. Multiplication (Type 4)")
    operation = int(input(" --> "))
    
    if operation == 1:
        print("The result of addition is: " , addition(num1, num2))
    
    elif operation == 2:
        print("The result of subraction is: " , subtraction(num1, num2))
    
    elif operation == 3: 
        print("The result of division is: " , division(num1, num2))
    
    elif operation == 4:
        print("The result of multuplication is: ", multiplication(num1, num2))
    
    else:
        print("Invalid output. Please select a valid operation.")
        
    
    cont_perm = input("Do you want to continue? (y/n): ")
    if cont_perm.lower() == 'y':
        continue
    else: 
        print("Thank you for using the calculator. Goodbye!")
        break    
    