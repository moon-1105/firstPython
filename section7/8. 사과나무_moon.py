import sys
from collections import deque
#sys.stdin = open("in.txt","r")

N = int(input())
tree = []
his = []
for _ in range(N):
    tree.append(list(map(int, input().split())))
    his.append([0]*N)

dir = [[1,0], [0,1], [-1,0], [0,-1]]
apple = 0
now = [N//2, N//2]

q = deque()
q.append(now)
his[now[0]][now[1]] = 1
apple += tree[now[0]][now[1]]
for _ in range( N//2 ):
    newq = deque()
    while q: # 안에 있으면...
        now = q.pop()
        # 방향으로 진행 가능하면 진행
        for d in dir:
            if 0<= now[0]+d[0] < N and 0<= now[1]+d[1] < N:
                next = [ now[0]+d[0], now[1]+d[1] ]
                if his[next[0]][next[1]] == 0:
                    newq.append(next)
                    apple += tree[next[0]][next[1]]
                    his[next[0]][next[1]] = 1
    q = newq.copy()
   # print("=============")
    #for ele in his:
    #    print(ele)
    #print("=============")

print(apple)






