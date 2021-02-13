import sys
sys.stdin=open("input.txt", "r")
from collections import deque

# 1개만 남을때까지 항상 K 번째 수(K의 배수)가 제거됨.
N, K = map(int, input().split())
dq = list(range(1, N+1))
dq = deque(dq)

while dq:
    for _ in range(K-1): #아무 변수 없이 반복
        cur = dq.popleft() # 맨 앞에거가 pop
        dq.append(cur) # 맨 뒤로 붙이기
    #이렇게 해서 K번 자리를 옮기게 하고
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
