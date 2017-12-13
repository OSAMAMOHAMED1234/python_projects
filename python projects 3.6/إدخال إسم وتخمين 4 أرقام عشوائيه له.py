from random import randint

while True :
    r = randint(0, 10000)
    name = input('name : ')
    def o(arg):
        res=[]
        res.append(arg)
        res.append(r)
        return res
    print(o(name))
