while True :
    n = int(input('Enter a number : '))
    def sum_even(n):
        total = 0
        for i in range(2, n+1, 2):
            total += i
        return total
    print(sum_even(n))

'''
def sum_even(n):
        if n < 1 :
            return 0
        elif n % 2 != 0 :
            return sum_even(n -1)
        else :
            return n + sum_even(n - 2)
    print(sum_even(n))
'''
