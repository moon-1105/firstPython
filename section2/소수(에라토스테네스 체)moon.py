# 소수(에라토스테네스 체)

N = int(input())

arr = [0]*(N+1)
arr[0] = 100
arr[1] = 100

num = 2
idx = num
while num <= N/2:
    배 = 2
    #print(num)
    idx = num * 배
    while idx <= N:
        arr[idx] = 100
        배+=1
        idx = 배 * num
        #print(idx, "=",배,"*",num)
    #print(arr)    
    num+=1

if N > 1:
    arr[2]=0
if N > 2:
    arr[3]=0
#print(arr)

cnt = 0
for num in arr:
    if num != 100:
        cnt+=1      

print(cnt)
