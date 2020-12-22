
import sys
#sys.stdin=open("in1.txt", "rt")

N, k = map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(1, len(a)):
    for j in range(i + 1, len(a)):
        for l in range(j + 1, len(a)):
            b.add(int(a[i] + a[j] + a[l]))
a = list(b)
a.sort(reverse=True)
print(a[k-1])
