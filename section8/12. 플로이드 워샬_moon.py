import sys
#sys.stdin = open("in.txt")
"""
모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값
"""

def printMap():
    for i in range(1, city+1):
        for j in range(1, city+1):
            print(ans[i][j], end=" ")
        print()

def findMin(A, B):
    if A == 'M' and 'M' in B:
        return 'M'
    elif A == 'M':
        return B[0]+B[1]
    elif 'M' in B:
        return A
    else:
        return min(A, B[0]+B[1])

if __name__ == "__main__":
    city, road = map(int, input().split())
    arr = []
    ans = []
    for _ in range(road):
        arr.append(list(map(int, input().split())))
        # [도시1, 도시2, 비용]
    #   INIT
    for _ in range(city+1):
        ans.append(['M']*(city+1))
    for ele in arr:
        ans[ele[0]][ele[1]] = ele[2]
    for i in range(1, city + 1):
        ans[i][i] = 0
    #printMap()

    # ans[i][j] = ans[i][k] + ans[k][j] => 중에 가장 작은값으로 계속 업데이트함.
    for i in range(1, city+1):
        for j in range(1, city+1):
            for idx in range(1, city+1):
                ans[i][j] = findMin(ans[i][j], [ans[i][idx] , ans[idx][j]])

    for i in range(1, city + 1):
        for j in range(1, city + 1):
            for idx in range(1, city + 1):
                ans[i][j] = findMin(ans[i][j], [ans[i][idx], ans[idx][j]])

    printMap()





