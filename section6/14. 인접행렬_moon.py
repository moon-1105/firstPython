# 정점의 수 N 간선의 수 M
N, M = map(int, input().split())
#N,M = 6, 9
mapInfo = []
for _ in range(0, M):
    mapInfo.append(list(map(int, input().split())))

#mapInfo = [[1, 2, 7],[1, 3, 4],[2, 1, 2],[2, 3, 5],[2, 5, 5],[3, 4, 5],[4, 2, 2],[4, 5, 5],[6, 4, 5]]
인접행렬 = []
for _ in range(0,N):
    인접행렬.append([0]*N)

def cal():
    global 인접행렬
    if len(mapInfo)==0:
        return
    now = mapInfo.pop()
    s, e, v = now[0], now[1], now[2]
    #print("map[",s,",",e,"]=",v)
    인접행렬[s-1][e-1] = v;
    cal()

def printMap(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print(arr[i][j],end=" ")
        print()

cal()
printMap(인접행렬)



