import sys
#sys.stdin = open("input.txt", "rt")

def 봉우리인가(arr, x, y):
    max = arr[x][y]
    if max <= arr[x+1][y]:
        return False
    elif max <= arr[x][y+1]:
        return False
    elif max <= arr[x-1][y]:
        return False
    elif max <= arr[x][y-1]:
        return False
    return True

N = int(input())
arr = []
arr.append([0]*(N+2))
for i in range(0,N):
    tmp = list(map(int, input().split()))
    tmp = [0]+ tmp + [0]
    arr.append(tmp)
arr.append([0]*(N+2))
#print(arr)
cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if 봉우리인가(arr, i ,j):
            #print("(",i,",",j,")",arr[i][j])
            cnt+=1
print(cnt)



