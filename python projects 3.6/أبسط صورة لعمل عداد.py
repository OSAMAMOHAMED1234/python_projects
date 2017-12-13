#n = []
ans = ""
class Answers():
    answercount = 0
    #n.append(ans)

    def __init__(self, ans):
        self.ans = ans

    def displayanswers(self):
        print("Your Answer number is : ", self.ans)

    def displaycount(self):
        Answers.answercount += 1
        print('Total Answers %d' % Answers.answercount)
while True:
    try:
        ans = int(input("Enter your Answer number : "))
        #n.append(ans)
        Answers(ans)
        Answers(ans).displayanswers()
        Answers(ans).displaycount()
    except:
        print("wrong format!")
        exit()
print()


class Answers():
    answercount = 0
    def displaycount(self):
        Answers.answercount += 1
        print('Total Answers %d' % Answers.answercount)
while True:
    ans = int(input("Enter your Answer number : "))
    Answers().displaycount()





