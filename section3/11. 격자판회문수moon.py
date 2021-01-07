import sys
#sys.stdin=open("input.txt", "rt")

def is회문(arr, x, y):
    tmp1 = [0]*5
    tmp2 = [0]*5
    idx = 0
    ans = 0
    for i in range(x, x+5):
        if i < 7:
            tmp1[idx] = arr[i][y]
            idx+=1
    if _is회문(tmp1):
        ans+=1
    idx = 0
    for i in range(y, y+5):
        if i < 7:
            tmp2[idx] = arr[x][i]
            idx+=1
    if _is회문(tmp2):
        ans+=1
    return ans

def _is회문(list1):
    if len(list1)!=5:
        return False
    if list1[0] != list1[4]:
        return False
    if list1[1] != list1[3]:
        return False
    return True


arr = []
for i in range(0,7):
    arr.append(list(map(int, input().split())))
cnt = 0
for i in range(0,7):
    for j in range(0, 7):
        cnt += is회문(arr, i, j)

print(cnt)

