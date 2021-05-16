"""
어떤 구역에서 다른 구역으로 등산을 할 때는 그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은
구역으로만 이동할 수 있도록 등산로를 설계하려고 합
출발지에서 도착지로 갈 수 있는 등산 경로가 몇 가지 인지
"""
import sys
#sys.stdin = open("in.txt","r")

def findStartEnd(mountain):
    s, e = [1000000, 0,0], [-1,0,0]
    for i in range(N):
        for j in range(N):
            if s[0] > mountain[i][j]:
                s[0] = mountain[i][j]
                s[1], s[2] = i, j
            if e[0] < mountain[i][j]:
                e[0] = mountain[i][j]
                e[1], e[2] = i, j
    return s, e

def isOkay(nowValue, next):
    if 0<= next[0] < N and 0<= next[1] < N:
        if mountain[next[0]][next[1]] > nowValue:
            if his[next[0]][next[1]] == 0:
                return True
count = 0
dir = [[1,0],[0,1],[-1,0],[0,-1]]
def cal(st, his, e):
    global count
    if len(st)==0:
        return
    now = st.pop()
    if now == e :
        #print("성공")
        count+=1
    for d in dir:
        next = [now[1]+d[0],now[2]+d[1]]
        if isOkay(now[0], next):
            st.append([mountain[next[0]][next[1]], next[0], next[1]])
            his[next[0]][next[1]] = 1
            cal(st, his, e)
            his[next[0]][next[1]] = 0

if __name__=="__main__":
    N = int(input())
    mountain = []
    his = []
    for _ in range(N):
        mountain.append(list(map(int, input().split())))
        his.append([0]*N)
    s, e = findStartEnd(mountain)
    #print(s, e)
    st = []
    st.append(s)
    cal(st, his, e)
    print(count)



