import sys
from collections import deque
#sys.stdin = open("in.txt","r")

"""
스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수
있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성
"""
now, cow = map(int, input().split())
dir = [1, -1, 5]
q = deque()
q.append(now)
his = [0]*10000
dis = [0]*10000

while(q):
    chk = q.pop()
    if chk == cow:
        print(dis[chk])
        break
    else:
        for i in range(3):
            next = chk+dir[i]
            if 1 <= next < 10000 and his[next] == 0:
                q.append(next)
                his[next] = 1
                dis[next] = dis[chk] + 1

