import sys
#sys.stdin = open("input.txt", "rt")
def findCnt(x):
    x = int(x)
    cnt = 0
    for i in range(1,x+1):
        if( x % i ==0):
            cnt+=1
    return cnt

str1 = input()
ans = ""
for ch in str1:
    if ch.isdigit():
        ans = ans+ch

print(int(ans))
print(findCnt(ans))