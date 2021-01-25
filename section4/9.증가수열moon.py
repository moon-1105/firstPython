import sys
#sys.stdin=open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

#왼쪽 혹은 오른쪽에서 하나를 가져와서 가장 긴 증가수열을 만든다
#이때 가져온 숫자는 거기서 제거한다.

L = arr[0]
R = arr[len(arr) - 1]
ans = ""
if L < R:
    now = L
    arr = arr[1:]
    ans+= "L"
else:
    now = R
    arr = arr[:-1]
    ans += "R"

while True:
    L = arr[0]
    R = arr[len(arr) - 1]
    if len(arr)== 0:
        break
    if L < R:
        if now < L:
            now = L
            arr = arr[1:]
            ans += "L"
        else:
            if now < R:
                now = R
                arr = arr[:-1]
                ans += "R"
            else:
                break
    else:
        if now < R:
            now = R
            arr = arr[:-1]
            ans += "R"
        else:
            if now < L:
                now = L
                arr = arr[1:]
                ans += "L"
            else:
                break
print(len(ans))
print(ans)