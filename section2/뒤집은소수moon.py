import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+0.5)+1):
        if x % i == 0 :
            return False
    return True

def reverse(x):
    tmp = ""
    for ch in x:
        tmp = ch + tmp
    return int(tmp)
        

N = int(input())
arr = list(map(int, input().split()))
for num in arr:
    rev = reverse(str(num))
    if isPrime(rev) and rev not in (0,1):
        print(rev, end=" ")
