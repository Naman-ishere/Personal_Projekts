def isArmstrong(num : int) :
    strNum = str(num)
    power = len(strNum)
    total = 0
    digits = list(map(int, strNum))
    for i in digits:
        var = i ** power
        total = total + var
    if total == num:
        return "It is an Armstrong Number."
    else:
        return "It is not an Armstrong Number."
 



x = int(input("Enter a number: "))
print(isArmstrong(x))
