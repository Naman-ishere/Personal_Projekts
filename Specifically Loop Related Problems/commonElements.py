def dupTerm(list1: list) :
    nonDupItems = []
    for i in list1:
        if i in nonDupItems:
            continue
        else:
            nonDupItems.append(i)
    nonDupItems = [int(x) for x in nonDupItems]
    return nonDupItems

common_elements  = []

nums1 = input("Enter the numbers: ").split(" ")
nums2 = input("Enter the numbers: ").split(" ")

nums1Good = dupTerm(nums1)
nums2Good = dupTerm(nums2)

for i in nums1Good:
    if i in nums2Good:
        common_elements.append(i)
    else: 
        continue

print(common_elements)