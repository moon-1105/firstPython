#import sys
#sys.stdin=open("in.txt", "r")

#동전종류 개수

N = int(input())
kind = list(map(int, input().split()))
목표 = int(input())

"""
N, 목표 = 5, 129
kind = [1,8,20,25,30]
"""
min = 1000000000
def cal(현재금액, 개수):
    global min
    if min <= 개수:
        return
    if 목표 == 현재금액 :
        #print(개수)
        if 개수 < min:
            min = 개수
            return
    if 목표 < 현재금액:
        return
    for i in range(N-1 , -1, -1):
        cal(현재금액 + kind[i], 개수 +1)

cal(0,0)
print(min)

