import sys
#sys.stdin = open("input.txt", "rt")

def check(x):
    L = len(x)
    x = x.upper()
    for i in range(0,int(L/2)):
        if x[i] != x[L-i-1]:
            return False
    return True

N = int(input())
arr = []
for i in range(0,N):
    arr.append(input())

cnt = 1
for word in arr:
    if(check(word)):
        print("#"+str(cnt)+" YES")
    else:
        print("#" + str(cnt) + " NO")
    cnt+=1

