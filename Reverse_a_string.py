# A function to reverse a string.
def Reverse(word):
    return word[::-1]

word = input("Enter a word: ")

print(f"word: {word}")
print(f"reversed: {Reverse(word)}")