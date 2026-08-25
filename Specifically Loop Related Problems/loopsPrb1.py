# Give output of the even numbers from 1 to input, then count of even numbers, count of odd numbers and their sum

x = int(input("Enter a number: "))
totalEven = 0
evenCount = 0
oddCount = 0
totalOdd = 0

for i in range(1, x+1):
    if i % 2 == 0:
        evenCount += 1
        totalEven = totalEven + i
    else:
        oddCount += 1
        totalOdd = totalOdd + i
    i+=1

print("Even count:", evenCount)
print("Odd count:", oddCount)
print("Total even:", totalEven)
print("Total odd:", totalOdd)