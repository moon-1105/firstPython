#미로를 탈출하는 최단경로의 경로수
import sys
from collections import deque
#sys.stdin = open("in.txt","r")

s, e = [0,0], [6,6]
his, maze =[], []
for _ in range(7):
    maze.append(list(map(int, input().split())))
    his.append([0]*7)

dir=[[1,0],[-1,0],[0,1],[0,-1]]
q = deque()
q.append(s)
his[s[0]][s[1]] = 1

def isOkay(next):
    if 0<= next[0]<7 and 0<=next[1]<7:
        if maze[next[0]][next[1]] == 0:
            if his[next[0]][next[1]] == 0:
                return True
    return False
flag = True
cnt = 0

while q:
    now = q.popleft()
    if now == e:
        flag = False
       # print("도착")
    for d in dir:
        next = [now[0]+d[0],now[1]+d[1]]
        if isOkay(next):
            q.append(next)
            his[next[0]][next[1]] = his[now[0]][now[1]]+1
    #print("=============")
    #for ele in his:
    #    print(ele)
    #print("=============")


if flag :
    print(-1)
else:
    print(his[6][6]-1)
