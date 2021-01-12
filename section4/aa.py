import sys
sys.stdin=open("input.txt", "rt")
# N개의 마구간이 수직선상에 있음( 좌표, 중복 X)
# C 마리의 말이 있는데 가장 가까운 말의 거리가 최대가 되게 말을 배치하고 싶음
# 가장 가까운 두 말의 거리가 최대가 되는 마구간 배치를 할때, 그 최대 거리는?
def findMax(마굿간, idx):
    minusDis, plusDis = 0, 0
    tmp = idx
    while True :
        tmp-=1
        minusDis+=1
        if tmp <= 0:
            break
        if 마굿간[tmp] == 1:
            break
    tmp = idx
    while True :
        tmp+=1
        plusDis+=1
        if tmp >= len(마굿간):
            break
        if 마굿간[tmp] == 1:
            break
    if( minusDis < plusDis):
        return minusDis
    else:
        return plusDis


def findNear(마굿간, 말):
    # 말이 채워진 마굿간이 주어졌을 때, 하나를 추가로 배치하려고 함.
    # 배치한 그 배열을 return 함.
    공간 = [0]*len(마굿간)
    for idx in range(0, len(마굿간)):
        if(말[idx]!=1): #말이 채워져있지 않다면 해당 idx에서 가장 가까운 거리를 체크함
            거리 = findMax(마굿간, idx)
            공간[idx] = 거리
    print(공간)
    최대거리 = 공간.index(max(공간))
    말[최대거리] = 1
    return 말

N, C = map(int, input().split())
arr = []
for i in range(0,N):
    arr.append(int(input()))
arr.sort()

if(C == 2):
    print(max(arr)-min(arr))
else:
    마굿간 = [0]*(max(arr)+1)
    말위치 = [0]*(max(arr)+1)
    for i in range(0, N):
        마굿간[arr[i]] = 1
    말위치[arr[0]] = 1
    말위치[arr[N-1]] = 1

    for i in range(0, C-2):
        말위치 = findNear(마굿간, 말위치)

    print(마굿간)
    print(말위치)

    공간 = [0] * len(마굿간)
    for i in range(0, len(마굿간)):
        if 말위치[i]==1:
            공간[i] = findMax(말위치, i)
    print("=========")
    print(공간)
    print(max(공간))