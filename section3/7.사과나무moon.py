import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr = []
for i in range(0, N):
    arr.append(list(map(int, input().split())))

개수 = 1
시작점 = int(N/2)

sum = 0
for i in range(0, int(N/2)):
    for j in range(0, 개수):
        #print(arr[i][시작점 + j], end=" ")
        sum += arr[i][시작점 + j]
    #print()
    개수+=2
    시작점-=1

for i in range(0, N):
    #print(arr[int(N/2)][i], end=" ")
    sum += arr[int(N/2)][i]
#print()

개수 = N-2
시작점 = 1
for i in range(int(N/2)+1, N):
    for j in range(0, 개수):
        #print(arr[i][시작점 + j], end=" ")
        sum += arr[i][시작점 + j]
    #print()
    개수-=2
    시작점+=1

print(sum)
