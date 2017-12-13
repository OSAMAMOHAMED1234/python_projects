from random import randint
answer = randint(0, 100)
print(answer)

print("let's play the game ! ")
while True :
    guess = int(input('Guess a number between 0 & 100 :'))
    if guess < answer :
        print("guess higher number!")
    elif guess > answer :
        print("guess lower number!")
    else:
        print("you are right!")
        break
