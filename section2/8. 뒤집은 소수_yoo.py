import sys
import math
#sys.stdin=open("in2.txt", "rt")

def reverse(x):
    a = 0
    while x > 0:
        a *= 10
        tmp = x % 10
        if tmp != 0:
            a += tmp
        x //= 10
    return a
def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    m = math.ceil(math.sqrt(x))
    for i in range(2, m + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
a = list(map(int, input().split()))
t = 0
b = []
for i in range(0, len(a)):
    t = reverse(a[i])
    if isPrime(t):
        b.append(t)
for i in range(0, len(b)):
    print(b[i], end=' ')
