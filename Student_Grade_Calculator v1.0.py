'''
From 0 to 30 = F
From 31 to 50 = D
From 51 to 70 = C
From 71 to 85 = B
From 86 to 95 = A
From 96 to 100 = A+
'''


totalMarks = 500
print("Welcome to King Naman's Student Grade Calculator")
print("This calculator is limited to 5 different Subjects only. Please don't cry if they aren't mentioned here. :)")
print("The Subjects are as follows:")
print("1. Mathematics")
print("2. Science")
print("3. English")
print("4. Computer Science")
print("5. Physical Education")

# In this code block, the inputs of marks will be taken from the user.
while True: 
    marksMath = int(input("Enter your marks in Mathematics: "))
    marksScience = int(input("Enter your maeks in Science: "))
    marksEnglish = int(input("Enter your marks in English: "))
    marksComp_Science = int(input("Enter your marks in Computer Science: "))
    marksPE = int(input("Enter your marks in Physical Education: "))
    
    totalMarksObtained = marksMath + marksScience + marksEnglish + marksComp_Science + marksPE
    avgScore_Student = totalMarksObtained / 5
    percentScore_Student = (totalMarksObtained / totalMarks) * 100
    
    if percentScore_Student >= 0 and percentScore_Student <= 30:
        grade = "F"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have FAILED!!") 
    elif percentScore_Student >= 31 and percentScore_Student <= 50:
        grade = "D"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have FAILED!!")
    elif percentScore_Student >= 51 and percentScore_Student <= 70:
        grade = "C"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have PASSED!!")
    elif percentScore_Student >= 71 and percentScore_Student <= 85:
        grade = "B"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have PASSED!!")
    elif percentScore_Student >= 86 and percentScore_Student <= 95:
        grade = "A"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have PASSED!!")
    else:
        grade = "A+"
        print("Your total score is:", totalMarksObtained, "out of", totalMarks)
        print("Your average score is:", avgScore_Student)
        print("Your percentage score is:", percentScore_Student,"%")
        print("Your grade is:", grade)
        print("You have PASSED!!")
    
    calculateAgain = input("Do you want to calculate again? (y/n): ")
    if calculateAgain.lower() != 'y':
        print("Thank you for using King Naman's Student Grade Calculator. Goodbye!")
        break
    else:
        print("Let's do it again.")
        continue