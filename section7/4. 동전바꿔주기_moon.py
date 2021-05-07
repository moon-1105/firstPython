import sys
sys.stdin=open("in.txt", "r")
"""
입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때
(i=1,2,...,k)
지폐를 동전으로 교환하는 방법의 가지 수를
"""
T = int(input())
K = int(input())
coin_v=[]
coin_m=[]
for _ in range(0,K):
    tmp = list(map(int, input().split()))
    coin_v.append(tmp[0])
    coin_m.append(tmp[1])
cnt = 0
def cal(idx, total):
    global cnt
    if T < total:
        return
    if idx == K:
        if total ==T:
            cnt+=1
    else:
        for i in range(0, coin_m[idx]+1):
            # 동전 0개, 1개, 2개,,, 씩 포함시켜서 돌리기
            cal(idx+1, total + (coin_v[idx]*i))

cal(0, 0)
print(cnt)