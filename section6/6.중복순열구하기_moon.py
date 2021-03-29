import sys
#sys.stdin=open("in.txt", "r")

# 1~N 까지 번호가 적힌 구슬. 중복을 허락하여 M 번을 뽑는 모든 경우의 수.
# N, M = map(int, input().split())
N, M = 3, 2
# 구슬
marbles = []
for num in range(1, N+1):
    marbles.append(num)

def printValid(arr):
    ans = {}
    tmp = []
    if arr.count(1) == M:
        for i in range(0, len(arr)):
            if arr[i] == 1:
                print(marbles[i], end=" ")
        print()

def dps(arr, now):
    if now > M:
        printValid(arr)
        return
    if now >= N:
        return
    """
    # 뽑았을 때
    arr[now] = 1
    dps(arr, now+1)
    # 안뽑았을 때
    arr[now] = 0
    dps(arr, now+1)
    """
    for i in range(1, N+1):
        arr[now] = 1
        dps(arr, now+1)
        arr[now] = 0
        dps(arr, now + 1)

dps([0]*N, 0)