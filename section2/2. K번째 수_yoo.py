
import sys
#sys.stdin=open("in1.txt", "rt")

T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for j in range(s - 1, e):
        b.append(a[j])

    b.sort()
    print("#%d %d" %(i+1, b[k-1]))
