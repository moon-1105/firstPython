import sys
#sys.stdin = open("input.txt", "rt")

def 모래시계출력(N, arr):
    sum = 0
    개수 = N
    시작점 = 0
    for i in range(0,int(N/2)):
        for j in range(시작점, 시작점+개수):
            #print(arr[i][j],end=" ")
            sum += arr[i][j]
        #print()
        개수 -= 2
        시작점 += 1
    #print(arr[int(N/2)][int(N/2)])
    sum += arr[int(N/2)][int(N/2)]
    개수 = 3
    시작점 = int(N/2)-1
    for i in range(int(N/2)+1, N):
        for j in range(시작점, 시작점 + 개수):
            #print(arr[i][j], end=" ")
            sum += arr[i][j]
        #print()
        개수 += 2
        시작점 -= 1

    return sum

def 회전(arr,행,N,방향,개수):
    tmp_list = [0]*N
    if 방향 == 0: #왼쪽
        for i in range(0,N):
            tmp_list[i] = arr[행-1][(i+개수)%N ]
        #print(arr[행-1], " ", tmp_list)
    else: #오른쪽
        for i in range(0,N):
            tmp_list[i] = arr[행-1][(i-개수)%N ]
        #print(arr[행 - 1], " ", tmp_list)

    for i in range(0, N):
        arr[행-1][i] = tmp_list[i]

    return arr

N = int(input())

arr = []
for i in range(0,N):
    arr.append(list(map(int, input().split())))



M = int(input())
rotate = []
for i in range(0,M):
    rotate.append(list(map(int, input().split())))


for i in range(0,M):
    arr = 회전(arr, rotate[i][0], N, rotate[i][1],rotate[i][2])

print(모래시계출력(N, arr))




