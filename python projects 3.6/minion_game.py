def minion_game(string):
  stuart_score , kevin_score = 0, 0
  sl = len(string)
  for l in range(sl) :
    if string[l] in 'AEIOU':
      kevin_score += (sl - l) #  6-1 6-3 6-5 => 5 3 1 = 9
    else:
      stuart_score += (sl - l) # 6-0 6-2 6-4 => 6 4 2 = 12
  if kevin_score > stuart_score:
    print('Kevin', kevin_score)
  elif kevin_score < stuart_score:
    print('Stuart', stuart_score)
  else:
    print('Draw')
    
minion_game('BANANA')