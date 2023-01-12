def palindrome(word):
  word = word.lower().strip()
  word_backwards = word[::-1]

  if word == word_backwards:
    return "This word is a palindrome"
  else:
    return "This word is not a palindrome"

print(palindrome("tacocat"))