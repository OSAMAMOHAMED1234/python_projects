while True :
    n = int(input('Enter a number : '))
    def sum_odd(n):
        total = 0
        for i in range(1, n+1, 2):
            total += i
        return total
    print(sum_odd(n))

'''
while True :
    n = int(input('Enter a number : '))
    def sum_odd(n):
        if n < 2 :
            return 1
        elif n % 2 == 0 :
            return sum_odd(n -1)
        else :
            return n + sum_odd(n - 2)
    print(sum_odd(n))
'''
