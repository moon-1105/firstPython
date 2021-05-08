import sys
#sys.stdin=open("in.txt", "r")
"""
N개의 동전을 A, B, C 세명에게 나누어 주려고 합니다.
세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰
사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
"""
N = int(input())
coin = []
for _ in range(N):
    coin.append(int(input()))
def differ(a, b, c):
    arr = [a, b, c]
    m = min(arr)
    M = max(arr)
    return M-m
ans= []
def cal(idx, A, B, C):
    global ans
    if idx == N :
        #print("A: ",A,"B: ",B,"C: ",C, end=" =>")
        if A!=B and B!=C and A!=C :
            ans.append(differ(A,B,C))
        return
    else:
        cal(idx+1, A+coin[idx], B, C)
        cal(idx + 1, A, B+coin[idx], C)
        cal(idx + 1, A, B, C+coin[idx])


cal(0,0,0,0)
print(min(ans))