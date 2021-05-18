import sys
from collections import deque
#sys.stdin = open("in.txt","r")

def isOkay(chk):
    if 0<= chk[0] < N and 0<= chk[1] <N:
        if chart[chk[0]][chk[1]] == 1:
            if his[chk[0]][chk[1]] == 0:
                return True
    return False

dir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
def bfs(q):
    global his
    while q:
        now = q.popleft()
       # print(now, end =" ")
        for d in dir:
            next = [now[0]+d[0],now[1]+d[1]]
            if isOkay(next):
                q.append(next)
                his[next[0]][next[1]] = 1

if  __name__ == "__main__":
    N = int(input())
    chart, his = [] , []
    for _ in range(N):
        chart.append( list(map(int, input().split())))
        his.append([0]*N)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if his[i][j] == 0 and chart[i][j] == 1:
                q = deque()
                q.append([i,j])
                his[i][j] = 1
                bfs(q)
                cnt+=1
   # for ele in his:
    #    print(ele)
    print(cnt)