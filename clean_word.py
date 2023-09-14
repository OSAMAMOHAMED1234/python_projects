def clean_word(word):
  if len(word) == 1:
    return word
  elif word[0] == word[1]:
    return clean_word(word[1:])
  return word[0] + clean_word(word[1:])

print(clean_word('wwwoooorrrldd'))