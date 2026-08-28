# In this problem we are going to find the second largest number and print it.
numbers = list(input().split(" "))
numbers = [int(x) for x in numbers]
biggestNum = 0
for i in numbers:
    if i > biggestNum:
        biggestNum = i
        biggie = [biggestNum]
    else:
        continue
    
    