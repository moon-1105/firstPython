import sys
#sys.stdin=open("in2.txt", "rt")

N = int(input())
for i in range(0, N):
    a = str(input())
    b = a.upper()
    if b == b[::-1]:
        print("#", end='')
        print(i+1, "YES")
    else:
        print("#", end='')
        print(i+1, "NO")
