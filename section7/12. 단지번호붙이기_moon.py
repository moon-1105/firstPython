import sys
#sys.stdin = open("in.txt","r")

"""
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
"""
class po:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = chart[x][y]

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

def isOkay(chk):
    if chart[chk.x][chk.y] == 1:
        if his[chk.x][chk.y] == 0:
            return True
    return False

dir = [[1,0],[0,1],[-1,0],[0,-1]]
def cal(st):
    global his
    if len(st) == 0:
        return
    else:
        now = st[ len(st)-1 ]
      #  print(now, end=" ")
        for d in dir:
            if 0 <= now.x+d[0] < N and 0 <= now.y+d[1] < N:
                next = po(now.x+d[0], now.y+d[1])
                if isOkay(next):
                    st.append(next)
                    his[next.x][next.y] = 1
                    cal(st)

if  __name__ == "__main__":
    N = int(input())
    chart = []
    his = []
    for _ in range(N):
        s = input()
        tmp = []
        for ch in s:
            tmp.append(int(ch))
            his.append([0]*N)
        chart.append(tmp)
    count = 0
    ans = []
    for i in range(N):
        for j in range(N):
            if (chart[i][j] != 0 and his[i][j] == 0):
                st = [po(i,j)]
                his[i][j] = 1
                cal(st)
                count+=1
                ans.append(len(st))

    print(count)
    ans.sort()
    for ele in ans:
        print(ele)


