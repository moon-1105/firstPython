# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램

N, F = map(int, input().split())
#N, F = 4, 16

num = []
for i in range(1, N+1):
    num.append(i)

stop = False
#순열구하기
def cal(arr):
    global stop
    if stop == True:
        ans = arr
        return
    if len(arr) == N:
        #print(arr)
        #답인지 체크하기
        if check(arr) == F:
            stop = True
            for ele in arr:
                print(ele, end=" ")
            return

    for n in num:
        if not n in arr:
            arr.append(n)
            cal(arr)
            arr.pop()

"""
1=> 1
2=> 1, 1
3=> 1, 2,  1
4=> 1, 3,  3, 1
5=> 1, 4,  6,  4, 1
6=> 1, 5, 10, 10, 5, 1
7=> 1, 6, 15, 20, 15, 1
"""
def makePakar(n):
    if n == 1:
        return n
    if n == 2:
        return [1, 1]
    map= []
    for i in range(0,n):
        map.append([0]*n)
    for i in range(0,n):
        map[i][0] = 1
        map[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            map[i][j] = map[i-1][j-1] + map[i-1][j]
    return map[n-1]



def printMap(map):
    for i in range(0, len(map)):
        for j in range(0, len(map)):
            print(map[i][j],end=" ")
        print()
    print()

def check(arr):
    sum = 0
    paskar = makePakar(N)
    for i in range(0,N):
        sum += arr[i]*paskar[i]
    return sum

cal([])
