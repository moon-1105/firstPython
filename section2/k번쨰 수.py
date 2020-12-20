import sys
#sys.stdin = open("input.txt", "rt")

T = int(input())
for case in range(T):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    mid = arr[s-1:e]
    mid.sort()

    print("#",case+1,mid[k-1])




