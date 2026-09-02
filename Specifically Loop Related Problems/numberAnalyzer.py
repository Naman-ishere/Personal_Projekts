nums = input("Enter the number: ").split(" ")
nums = [int(x) for x in nums]
noOfDigs = len(nums)
largestNum = 0
evenNums = []
oddNums = []

# For the largest digit
for larNum in nums:
    if larNum > largestNum:
        largestNum = larNum
    else:
        continue
    
# Largest number has been found
# Now we will work onto something which annoys the shit out of me. 

mediator = largestNum
lowestNum = 0

for j in nums:
    if j <= mediator:
        mediator = j
        lowestNum = mediator
    else:
        continue
    
print(lowestNum) 
# We have found the lowest number using this                               

# Now we have to find the even digits and odd digits

for k in nums:
    if k % 2 == 0:
        evenNums.append(k)
    else:
        oddNums.append(k)
        
        
        
        
# The whole output block
print("Number of digits:", noOfDigs)
print("Sum of Digits:", sum(nums))
print("Largest Digit:", largestNum)
print("Smallest Digit:", lowestNum)
print("Even Digits:", len(evenNums))
print("Odd Digits:", len(oddNums))