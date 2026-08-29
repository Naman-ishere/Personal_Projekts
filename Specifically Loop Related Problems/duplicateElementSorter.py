nums = input("Enter the numbers: ").split(" ")
nums = [int(x) for x in nums]
nonDup = []

for i in nums:
    if i in nonDup:
        continue
    else:
        nonDup.append(i)
print(nonDup)