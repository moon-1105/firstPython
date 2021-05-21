import sys
#sys.stdin = open("in.txt","r")
from collections import deque
"""
현수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
"""
def allRipen(tomato):
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return False
    return True
def findRipen(field):
    ripen = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                ripen.append([i, j])
    return ripen

def printField():
    print("=============")
    for ele in field:
        print(ele)
    print("=============")

def nextDay(q, days):
    nextTomato =deque()
    while q:
        now = q.popleft()
        for d in dir:
            if 0 <= now[0] + d[0] < N and 0 <= now[1] + d[1] < M:
                next = [now[0] + d[0], now[1] + d[1]]
                if field[next[0]][next[1]] == 0:
                    nextTomato.append([next[0], next[1]])
                    field[next[0]][next[1]] = 1
    return nextTomato

dir = [[1,0],[0,1],[-1,0],[0,-1]]
def cal(field):
    q = deque()
    ripen = findRipen(field)
    if len(ripen)==0:
        return -1
    else:
        for ele in ripen:
            q.append(ele)
        days = 0
        while not allRipen(field):
            q = nextDay(q, days)
            if len(q) == 0:
                return -1
           # printField()
            days += 1

    return days

if __name__ == "__main__":
    M, N = map(int, input().split())
    field = []
    #tomato =[]
    for _ in range(N):
        field.append(list(map(int, input().split())))
        #tomato.append([0]*M)
    days = cal(field)
    print(days)

