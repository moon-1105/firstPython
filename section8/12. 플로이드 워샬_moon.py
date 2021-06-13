import sys
sys.stdin = open("in.txt")
"""
모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값
"""
def canGo(i,j):
    for ele in arr:
        if ele[0]==i and ele[1]==j:
            return ele[2]
    return -1

def findShort(idx):
    m = 1000000
    chk = False
    for j in range(1, city+1):
        if ans[j][idx] != 'M':
            m = min(m, ans[j][idx])
            chk = True
    if chk:
        return m
    else:
        return 0

if __name__ == "__main__":
    city, road = map(int, input().split())
    arr = []
    ans = []
    for _ in range(road):
        arr.append(list(map(int, input().split())))
        # [도시1, 도시2, 비용]
    for _ in range(city+1):
        ans.append(['M']*(city+1))

    for i in range(1, city+1):
        for j in range(1, city+1):
            # i 에서 j로
            # j로 가는 비용 + [i까지 가장 짧은 길]
            v = canGo(i, j)
            if  v != -1 :
                ans[i][j] = findShort(i) + v
            else:
                ans[i][j] = 'M'
        for ele in ans:
            print(ele[1:])
        print("=====================")
    for i in range(1, city + 1):
        ans[i][i] = 0





