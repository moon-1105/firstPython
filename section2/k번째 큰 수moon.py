import sys
#sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
#print(arr)
ans = []

#꼭 순서대로 뽑는게 답이라는 보장이 없음
for first in range(0,N):
    if len(ans) == K+5:
        break
    fir = arr[first]
    for second in range( first+1, N ) :
        sec = arr[second]
        for third in range( second+1, N):
            thi = arr[third]
            ans.append (fir + sec + thi)
    #print(ans)

ans = set(ans)
ans = list(ans)
ans.sort(reverse = True)
#print(ans)
print(ans[K-1])
