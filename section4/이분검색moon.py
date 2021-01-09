import sys
#sys.stdin=open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
target = arr[int(N/2)]
idx = 0
if target == M:
    print(int(N/2)+1)
else:
    while target != M :
        mid = int(len(arr) / 2)
        target = arr[mid]
        if M < target:
            arr = arr[0:mid]
        else:
            arr = arr[mid:]
            idx += mid
    print(idx+1)