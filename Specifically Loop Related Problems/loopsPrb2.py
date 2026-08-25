# I am making a divisibility detector

# Input: A number

# Output: Three lists - one for numbers divisible by 3, one for numbers divisible by 5, and one for numbers divisible by both 3 and 5


inpUs = int(input("Enter a number: "))
divBy3 = []
divBy5 = []
divBy3n5 = []


for i in range(1, inpUs + 1):
    StrI = str(i)
    chars = list(StrI)
    digits = [int(x) for x in StrI]
    totalAdd = sum(digits)
    if totalAdd % 3 == 0 and i % 5 == 0:
        print(i)
        divBy3n5.append(i)
    elif totalAdd % 3 == 0:
        print(i)
        divBy3.append(i)
    elif i % 5 == 0:
        print(i)
        divBy5.append(i)
    else:
        None 

print("Divisible by 3:", divBy3)
print("Divisible by 5:", divBy5)
print("Divisible by 3 and 5:", divBy3n5)

