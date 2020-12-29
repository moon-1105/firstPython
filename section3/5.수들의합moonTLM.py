import sys
#sys.stdin = open("input.txt", "rt")

def cal( arr, start, end, M):
    sum = 0
    for idx in range(start, end+1):
        if sum > M :
            return -1
        sum+=arr[idx]
    return sum
N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = sum(arr)
cnt = 0
for start in range(0, N):
    for end in range(start, N):
        if( cal(arr, start, end, M) == M):
           # print(start,"~",end)
            cnt += 1
            s - M
    if(s < M):
        break


print(cnt)