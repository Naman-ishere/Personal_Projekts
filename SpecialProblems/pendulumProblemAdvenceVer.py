numStr = list(input("Enter the numbers: ").split(" "))
numbers = [int(x) for x in numStr]
biggestNum = 0
pendulumSolution = []

while True: 
    for x in range(1, len(numbers)+1):               #This block of code helps us find the biggest number and stores it inside the list.
        for bigboii in numbers:                       
            if bigboii > biggestNum:
                biggestNum = bigboii
        pendulumSolution.append(biggestNum)
        numbers.pop(numbers.index(biggestNum))



#   =================END PART================
    if len(pendulumSolution) == len(numbers):
        break
    else:
        continue
print(pendulumSolution)