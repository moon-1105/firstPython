import sys
#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if N%i == 0:
        cnt+=1
        #print(i, end=" ")
    if cnt == K:
        break;

if cnt < K :
    print(-1)
else:
    print(i)


