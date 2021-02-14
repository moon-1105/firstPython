import sys
sys.stdin=open("input.txt", "r")
from collections import deque

# 수업계획이 올바른지 아닌지 판단

tmp_must = input()
N = int(input())
schedule = []
for _ in range(0,N):
    schedule.append(input())
#print(schedule)

must = []
for ch in tmp_must:
    must.append(ch)
must = deque(must)

def isRight(sche):
    for ch in sche:
        #print(ch,end="를 이제 검사할 것  => ")
        if must:
            obj = must.popleft()
        else:
            return "YES"
        if obj != ch :
            must.appendleft(obj)
            #print()
        #else:
        #    print("일치하니까 이제 제외")
    if must :
        return "NO"
    else:
        return "YES"


for idx in range(1,N+1):
    print("#",end="")
    print(idx,isRight(schedule[idx-1]))
    must= []
    for ch in tmp_must:
        must.append(ch)
    must = deque(must)
