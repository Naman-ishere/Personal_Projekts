# This is a version of a multiplication table that gives me the table from 1 to whatever number entered by the user.

n = int(input("Enter the number you want to generate the table: "))

for i in range(1, n +  1):
    for j in range(1 , 11):
        multiply = i * j
        print(f"{i} x {j} = {multiply}")
        
    print("......................")