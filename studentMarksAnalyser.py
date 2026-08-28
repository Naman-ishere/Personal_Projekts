# Step 1: How many students passed
# Step 2: Give the specific sets of outputs. 

noOfStu = int(input("Enter the number of students: "))
marks = []
highestmarks = 0
lowestnum = 0
print("Enter the marks of the students below: ")
for i in range(1, noOfStu + 1):
   indiMarks = int(input())
   marks.append(indiMarks)

for j in marks:
    if j > highestmarks:
        highestmarks = j
    else: 
        continue
    
lowestnum = min(marks)
    
print(highestmarks)
print(lowestnum)


       