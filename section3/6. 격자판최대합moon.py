import sys
#sys.stdin = open("input.txt", "rt")

def 행의합(N, arr):
    max = -1
    for i in range(0,N):
        sum = 0
        for j in range(0,N):
            sum += arr[i][j]
        if(max < sum):
            max = sum
    return max

def 열의합(N, arr):
    max = -1
    for i in range(0, N):
        sum = 0
        for j in range(0, N):
            sum += arr[j][i]
        if (max < sum):
            max = sum
    return max

def 좌대각선의합(N, arr):
    sum = 0
    for i in range(0, N):
        sum += arr[0+i][0+i]
    return sum

def 우대각선의합(N, arr):
    sum = 0
    for i in range(0, N):
        sum += arr[N-1-i][N-1-i]
    return sum


N = int(input())

arr = []
for i in range(0, N):
    arr.append(list(map(int, input().split())))

ans = 행의합(N, arr)
tmp = 열의합(N, arr)
if ans < tmp:
    ans = tmp
tmp = 좌대각선의합(N, arr)
if ans < tmp:
    ans = tmp
tmp = 우대각선의합(N, arr)
if ans < tmp:
    ans = tmp

print(ans)