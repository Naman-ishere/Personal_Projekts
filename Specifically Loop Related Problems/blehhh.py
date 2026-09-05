toCheck = input("Enter the numbers: ").split(" ")
toCheck = [int(x) for x in toCheck]
count = 0
totalLen = len(toCheck)
countLast = 1
palindrome = ""

while True:
    if count < totalLen // 2:
        if toCheck[count] == toCheck[totalLen - countLast]:
            palindrome = "Yes"
            countLast += 1; count += 1;
        else:
            palindrome = "No"
            break
    else:
        break
    

print(palindrome)