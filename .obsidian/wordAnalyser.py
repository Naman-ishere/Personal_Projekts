sentence = input("Enter a sentence: ")
lenOfSentence = len(sentence)
print("Characters:", lenOfSentence)
print("Spaces:", sentence.count(" "))

# Number of words
words = sentence.split(" ")
print("Words:", len(words))
print("'a':", sentence.count('a'))
print("'e':", sentence.count('e'))

