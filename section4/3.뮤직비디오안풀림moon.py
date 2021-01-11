import sys
sys.stdin=open("input.txt", "rt")
# DVD에 N개의 곡
# 라이브 순서 유지되어야함.
# M 개의 최소 크기 DVD를 발매 - 그 크기는?

def get개수(arr, 크기):
    tmp = 0
    tmpList= []
    for dvd in arr:
        if (tmp+dvd) > 크기:
            tmpList.append(tmp)
            tmp = dvd
        elif tmp + dvd == 크기:
            tmp += dvd
            tmpList.append(tmp)
            tmp = 0
        else:
            tmp+=dvd
    return len(tmpList)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

크기 = sum(arr)
max = sum(arr)
min = min(arr)
while(True):
    ans = get개수(arr, 크기)
    if(ans == M):
        print(크기)
        break
    else:
        if ans < M: #크기를 더 줄여야함
            크기 = int((max+min)/2)
            max = 크기-1
        else:
            크기 = int((max + min) / 2)
            min = 크기+1

print(크기)