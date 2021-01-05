
import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
answer = ""
last = 0
while arr:
    if arr[0] > last and arr[len(arr) - 1] > last:
        if arr[0] < arr[len(arr) - 1]:
            last = arr[0]
            arr.remove(arr[0])
            answer += 'L'
        else:
            last = arr[len(arr) - 1]
            arr.remove(arr[len(arr) - 1])
            answer += 'R'
    elif arr[0] > last:
        last = arr[0]
        arr.remove(arr[0])
        answer += 'L'
    elif arr[len(arr) - 1] > last:
        last = arr[len(arr) - 1]
        arr.remove(arr[len(arr) - 1])
        answer += 'R'
    else:
        break
    cnt += 1
print(cnt)
print(answer)
