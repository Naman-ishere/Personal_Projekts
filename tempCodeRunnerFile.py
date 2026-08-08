
        print("The result of subraction is: ",subtraction(num1, num2))
    elif operation == 3: 
        print("The result of division is: ",division(num1, num2))
    elif operation == 4:
        print("The result of multuplication is: ",multiplication(num1, num2))
    else:
        print("Invalid output. Please select a valid operation.")
        
    
    cont_perm = input("Do you want to continue? (y/n): ")
    if cont_perm.lower() == 'y':
        continue
    else: 
        print("Thank you for using the calculator. Goodbye!")
        break    