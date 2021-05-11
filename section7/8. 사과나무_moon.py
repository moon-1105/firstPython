import sys
from collections import deque
sys.stdin = open("in.txt","r")

N = int(input())
tree = []
for _ in range(N):
    tree.append(list(map(int, input().split())))
his = [[0]*N]*N

dir = [[1,0], [0,1], [-1,0], [0,-1]]
apple = 0
now = [N//2, N//2]

q = deque()
q.append(now)
for _ in range( N//2+1 ):
    now = q.pop()
    for d in dir:
        if 0<= now[0]+d[0] < N and 0<= now[1]+d[1] < N:
            next = [ now[0]+d[0], now[1]+d[1] ]
            print(next)
            if his[next[0]][next[1]] == 0:
                print("hi")
                q.append(next)
                apple += tree[next[0]][next[1]]
                his[next[0]][next[1]] = 1
    print("=============")
    for ele in his:
        print(ele)
    print("=============")
print(apple)






