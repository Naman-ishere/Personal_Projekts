correctPin = "4321"
attempts = 0
maxAttempts = 3
acces_granted = False

while attempts < maxAttempts:
    entered_password = input("Enter the password: ")
    attempts += 1
    if entered_password == correctPin:
        print("Succesfull Login.")
        acces_granted = True
        break
    else: 
        print("Incorrect password. Try again.")
        continue
    
        