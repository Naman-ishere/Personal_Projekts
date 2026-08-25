text = input("Enter some word: ")
shift = int(input("Enter the shift value: "))
result = ""

if shift > 26:
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
            
print("Encrypted String: ", result)