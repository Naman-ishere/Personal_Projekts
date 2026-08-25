vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ")
characters = list(word)
vowelCount = 0
consonantCount = 0

for i in characters:
    if i in vowels:
        vowelCount += 1
    else:
        consonantCount += 1

if vowelCount > consonantCount:
    print("Number of vowels: ", vowelCount)
    print("Number of consonants: ", consonantCount)
    print("Number of vowels is more than consonants.")
else:
    print("Number of consonants: ", consonantCount)
    print("Number of vowels: ", vowelCount)
    print("Number of consonants is more than vowels.")