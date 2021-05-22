import sys
#sys.stdin = open("in.txt","r")

"""
0은 빈칸, 1은 집, 2는 피자집으로 표현
피자집 M개를 선택하는 기준으로 도시의 피자배달거리가 최소가 되는
M개의 피자집을 선택하려고 합니다
"""
class pos:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __str__(self):
        return "["+str(self.x)+", "+str(self.y)+"]"

def getDistance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def findPizzaDis(home, arr):
    min = 1000000000
    for ele in arr:
        tmp = getDistance(ele, home)
        if min > tmp:
            min = tmp
    return min

def calDistance(arr):
    dis = 0
    for h in home:
        dis += findPizzaDis(h, arr)
    return dis

minPizzaDis = 100000000
def sol(idx, arr):
    global minPizzaDis
    if len(arr) == M:
        #for ele in arr:
        #    print(ele, end=" ")
        pizzaDis = calDistance(arr)
        #print("=>",pizzaDis)
        if pizzaDis < minPizzaDis:
            minPizzaDis = pizzaDis
        return
    if idx >= len(pizza):
        return
    arr.append(pizza[idx])
    sol(idx+1, arr)
    arr.pop()
    sol(idx + 1, arr)

if __name__=="__main__":
    N, M = map(int, input().split())
    city = []
    for _ in range(N):
        city.append(list(map(int, input().split())))
    pizza, home = [], []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                pizza.append( pos(i,j) )
            if city[i][j] == 1:
                home.append(pos(i,j))
    sol(0, [])
    print(minPizzaDis)