import sys
import math
#sys.stdin=open("in2.txt", "rt")

def check(arr, num):
    count = 0
    for j in range(0, 3):
        if arr[num][j] == arr[num][j + 4] and arr[num][j+1] == arr[num][j + 3]:
            count += 1
        if arr[j][num] == arr[j + 4][num] and arr[j+1][num] == arr[j + 3][num]:
            count += 1
    return count


arr = [[int(x) for x in input().split()]for y in range(7)]
answer = 0
for i in range(0, 7):
    answer += check(arr, i)
print(answer)
