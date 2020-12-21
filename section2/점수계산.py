import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
sum = arr[0]
add = 0
for i in range(1, N):
    if arr[i]==1 and arr[i-1] == arr[i]:
        add += 1
        sum += arr[i]+add
    else:
        add = 0
        sum += arr[i]
    #print(i+1 ," : ",sum)

print(sum)



