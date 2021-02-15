import sys

#sys.stdin = open('in1.txt', 'r')

def f_check(number):
    if l[number] > 0:
        return l[number]
    if number == 0:
        return 1
    elif number == 1:
        return 2
    else:
        l[number] = f_check(number - 1) + f_check(number - 2)
        return l[number]

N = int(input())
l = [0] * N
print(f_check(N-1))
