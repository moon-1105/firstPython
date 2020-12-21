import sys
#sys.stdin = open("input.txt", "rt")

def digit_sum(num):
    tmp = str(num)
    val = 0
    for ch in tmp:
        val += int(ch)
    return val

N = int(input())
arr = list(map(int, input().split()))
ans = []
max = -1
for num in arr:
    val = digit_sum(num)
    ans.append([num, val])
    if max < val:
        max = val

for numSet in ans:
    if numSet[1] == max:
        print(numSet[0])
        break
