def vowel_count(word):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    total = 0
    for i in word:
        if i in vowels:
            total += 1
    return total

word = input("Enter word: ")
print((f"Number of vowels: {vowel_count(word)}"))