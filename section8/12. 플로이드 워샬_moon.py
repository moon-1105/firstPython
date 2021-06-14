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
def printMap():
    for i in range(1, city+1):
        for j in range(1, city+1):
            print('{0:2d}'.format(ans[i][j]), end=" ")
        print()
    print("=====================")

if __name__ == "__main__":
    city, road = map(int, input().split())
    arr = []
    ans = []
    for _ in range(road):
        arr.append(list(map(int, input().split())))
        # [도시1, 도시2, 비용]
    #   INIT
    for _ in range(city+1):
        ans.append([50]*(city+1))
    for ele in arr:
        ans[ele[0]][ele[1]] = ele[2]

    for i in range(1, city+1):
        for j in range(1, city+1):
            # i 에서 j로
            # j로 가는 비용 + [i까지 가장 짧은 길]
            ans[i][j] = min(findShort(i), ans[i][j])

        printMap()

    for i in range(1, city + 1):
        ans[i][i] = 0






