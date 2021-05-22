import sys
#sys.stdin = open("in.txt","r")

"""
현수는 특정도착지점으로 도착하기 위해서는 몇 번째
열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다
"""
class pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        tmp = "["+str(self.x) +"," + str(self.y) +"]"
        return tmp

def isOkay(chk):
    if 0<= chk.x <10 and 0<= chk.y <10:
        if his[chk.x][chk.y] == 0:
            if ladder [chk.x][chk.y] in [1, 2]:
                return True
    return False

dir = [[0,1],[0,-1],[1,0]]
ans = -1
def findWay(now, his):
    global ans
    #print(now, end="=>")
    if now.x == 9 :
        if ladder[now.x][now.y] == 2:
            ans = start
            return True
        else:
            return False
    else:
        for d in dir:
            next = pos(now.x +d[0], now.y+d[1])
            if isOkay(next):
                his[next.x][next.y] = 1
                findWay(next, his)
                break

if __name__ == "__main__":
    ladder, his = [], []
    for _ in range(10):
        ladder.append(list(map(int, input().split())))
        his.append([0]*10)

    for start in range(10):
        if ladder[0][start] == 1:
            findWay(pos(0,start), his)
        his = []
        for _ in range(10):
            his.append([0] * 10)
    print(ans)
