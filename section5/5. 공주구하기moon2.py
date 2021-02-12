import sys
sys.stdin=open("input.txt", "r")


# 1개만 남을때까지 항상 K 번째 수(K의 배수)가 제거됨.
N, K = map(int, input().split())

q = []
for idx in range(1, N+1) :
    q.append(idx)

chk = 0
while len(q) != 1:
    if idx == len(q):
        idx = 0
    chk+=1
    # idx 로 체크했더니 ...?
    if chk % K == 0:
        q.remove(q[idx])
        #print(q)
    else:
        idx+=1

print(q[0])