
import sys
import math
from collections import deque

#sys.stdin = open("in1.txt", "rt")

N, K = map(int, input().split())
l = list(map(int, input().split()))
dq = deque(l)
m = 0
cnt = 0
while True:
    m = max(l)
    tmp = dq.popleft()
    if m == tmp:
        cnt += 1
        l.remove(tmp)
        if K == 0:
            break
    else:
        dq.append(tmp)
    if K == 0:
        K = len(l)
    K -= 1
print(cnt)
