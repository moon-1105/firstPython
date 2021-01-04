import sys
#sys.stdin = open("input.txt", "rt")

arr = []
for i in range(0,10):
    arr.append(list(map(int, input().split())))

ans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for item in arr:
    first = ans[:item[0]-1]
    mid = ans[item[0]-1:item[1]]
    last = ans[item[1]:]

    ans = []
    if first != None:
        ans += first

    if mid != None :
        mid.reverse()
        ans += mid

    if last !=None:
        ans +=last

for ch in ans:
    print(ch,end=" ")




