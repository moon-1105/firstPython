import sys
#sys.stdin = open("input.txt", "rt")


def check네모(arr, x, y):
    chk = [0] * 10
    for i in range(x, x+3):
        for j in range(y, y + 3):
            #print(arr[i][j], end=" ")
            chk[arr[i][j]] = 1
        #print()
    for i in range(1, 10):
        if chk[i] != 1:
            return False
    return True

def check행(arr, 행):
    chk = [0]*10
    for i in range(0,9):
        chk[arr[행][i]] = 1
    for i in range(1, 10):
        if chk[i] != 1:
            return False
    return True

def check열(arr, 열):
    chk = [0]*10
    for i in range(0,9):
        chk[arr[i][열]] = 1
    for i in range(1, 10):
        if chk[i] != 1:
            return False
    return True
arr=[]
for i in range(0,9):
    arr.append(list(map(int, input().split())))
#print(arr)
val = "YES"

for i in range(0,9):
    if not check행(arr, i):
        #print(i,"번쨰 행")
        val = "NO"
    if not check열(arr, i):
        #print(i, "번쨰 열")
        val = "NO"

for i in range(0,9,3):
    for j in range(0, 9, 3):
        if not check네모(arr, i, j):
            val = "NO"


print(val)

