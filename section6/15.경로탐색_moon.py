"""
방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요
"""
from inspect import stack

def printMap(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            print(arr[i][j],end=" ")
        print()

N,M = map(int, input().split())
route = []
for _ in range(N+1):
    route.append([0]*(N+1))
for _ in range(M):
    tmp = list(map(int, input().split()))
    route[tmp[0]][tmp[1]] = 1
#printMap(route)

cnt = 0
def dfs(val, his):
    global cnt
    if val == N:
        cnt+=1
        #print(his)
        return
    for i in range(1, N+1):
        if i not in his and route[val][i] == 1:
            his.append(i)
            dfs(i, his)
            his.pop()
    return

dfs(1, [1])
print(cnt)