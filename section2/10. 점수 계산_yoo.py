import sys
#sys.stdin=open("in2.txt", "rt")

N = int(input())
a = list(map(int, input().split()))
c = 0
answer = 0
for i in range(0, len(a)):
    if i == len(a) - 1:
       if a[i] == 1:
           c += 1
           for j in range(1, c + 1):
               answer += j
    if a[i] == 1:
        c += 1
    else:
        for j in range(1, c + 1):
            answer += j
        c = 0
print(answer)
