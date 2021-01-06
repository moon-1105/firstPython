
import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = str(input())
N = list(map(str, N))
cnt = 0
check = False
answer = 0
for i in range(len(N)):
    if N[i] == '(':
        cnt += 1
        check = True
    else:
        cnt -= 1
        if check:
            answer += cnt
        else:
            answer += 1
        check = False
print(answer)
