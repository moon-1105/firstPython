import sys
sys.stdin=open("input.txt", "r")

# 1개만 남을때까지 항상 K 번째 수가 제거됨.
N, K = map(int, input().split())

q = []
dq = []
for idx in range(1, N+1) :
    q.append(idx)
chk = 0
while len(q) > K-1 :
    idx = 0
    afterArr = []
    beforeArr = []
    for num in range(0, N):
        if q and idx < N-K-chk:
            afterArr.append(q.pop())
        elif q and idx == N-K-chk:
            tmp = q.pop()
            #print(tmp,"나간다")
        elif q and idx > N-K-chk:
            beforeArr.append(q.pop())
        idx+=1
    dq = beforeArr + afterArr
    while dq:
        q.append(dq.pop())
    #print("q=>",q)
    chk+=1
print(q)
print(q.pop())




