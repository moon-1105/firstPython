import sys
import math
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
sum = 0
for score in arr:
    sum += score
avg = round(sum/N)
print(avg,end=" ")

arr2=[]
for idx in range(0, N):
    arr2.append(abs(arr[idx] - avg))

near = float("inf")
near_idx = 0
near_arr = []

for idx in range(0, N):
    if arr2[idx] < near:
        near = arr2[idx]
        near_idx = idx

for idx in range(0, N):
    if near == arr2[idx]:
        near_arr.append([idx+1, arr[idx]-avg])

if(len(near_arr) == 1):
    print(near_arr[0][0])
else:
    for ele in near_arr:
        if ele[1] < 0 :
            continue
        else:
            print(ele[0])
            break
