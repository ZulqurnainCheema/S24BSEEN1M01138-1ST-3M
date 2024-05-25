given_word=input("Provide your word:")
given_symbol =input("Provide the symbol to replace with:")
def vowel_replacer(word,symbol):
  vowels = ["a", "e", "i", "o", "u"]
  result = ""
  for letter in word:
    if letter in vowels:
      result += symbol
    else:
      result += letter
  return result
print(vowel_replacer(given_word,given_symbol))
