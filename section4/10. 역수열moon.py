import sys
#sys.stdin=open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
num = []
for i in range(0, N):
    num.append((i+1, arr[i]))

ans = [0]*(N+1)
for nums in num:
    chk, idx = 0 , nums[1]+1
    target = nums[1]+1
    while chk <= target:
        #print("nums[",chk,"]",ans[chk],"검사")
        if ans[chk] != 0:
            idx+=1
            target+=1
        chk+=1
    ans[idx] = nums[0]

for idx in range(1, N+1):
    print(ans[idx], end=" ")