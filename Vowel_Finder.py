given_word = input("Enter a word: ")

def vowel_counter(word):
    result = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter in vowels:
            result += 1
    return result

number = vowel_counter(given_word)
print("Number of vowels:", number)
