import sys
from collections import deque
#sys.stdin = open("in.txt","r")
"""
그 다음에 그 지역에 많은 비가 내렸을 때 물에
잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사

물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은
왼쪽으로 인접해 있으며 그 크기가 최대인 영역
"""
def isOkay(chk, M):
    if 0<= chk[0]<N and 0<=chk[1]<N:
        if his[chk[0]][chk[1]] == 0:
            if area[chk[0]][chk[1]] > M:
                return True
    return False

def findGroup(q, his, M):
    while q:
        now = q.popleft()
        #print(now, end="->")
        for d in dir:
            next = [now[0] + d[0], now[1] + d[1]]
            if isOkay(next, M):
                q.append(next)
                his[next[0]][next[1]] = 1

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def cal(M):
    count = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > M and his[i][j] == 0:
                q = deque()
                q.append([i,j])
                his[i][j] = 1
                findGroup(q, his, M)
                count += 1
                #print()
    return count

if __name__ == "__main__":
    N = int(input())
    area, his = [], []
    for _ in range(N):
        area.append(list(map(int, input().split())))
        his.append([0]*N)
    rain = 0
    M = max(max(area))
    cnt, ans = 0, 0
    for rain in range(1, M):
        cnt = cal(rain)
        if cnt > ans:
            ans = cnt
        his = []
        for _ in range(N):
            his.append([0] * N)
    print(ans)