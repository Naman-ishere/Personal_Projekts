# Stored Credentials
password = "4321"

# Password detector starts from here
totalAttempts = 3
attemptsList = []


while True:
    inpUserPW = input("Enter your password: ")
    attempt = inpUserPW
    attemptsList.append(attempt)

    if inpUserPW == password:
        print("Login Successful!")
        break
    else:
        print("Wrong password.")
        totalAttempts = totalAttempts - 1
        print("Total attempts remaining:", totalAttempts)

        if totalAttempts == 0:
            print("Too many unsuccessful attempts. You have been locked out of the account")
            print("Try later, alligator")
            break
        else:
            continue
