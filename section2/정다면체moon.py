import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

dic = {}
max = -1
for n in range(1,N+1):
    for m in range(1, M+1):
        tmp = n+m
        if tmp in dic :
            dic[tmp] = dic[tmp]+1
        else:
            dic[tmp] = 1
        if max <  dic[tmp] :
            max =  dic[tmp]

#print(dic)
#print(max)

for num in dic:
    if dic.get(num) == max :
        print(num, end=" ")



