import sys

#sys.stdin=open("input.txt", "rt")
# 노래의 순서가 바뀌면 안됨.!!!
# M개에 다 녹음이 가능한데, DVD의 크기를 최소로해야함.

def findAns(amount):
    c = 1
    tmp = 0
    for i in music:
        if i + tmp > amount:
            tmp = i
            c += 1
        else:
            tmp += i
    return c

N, M = map(int, input().split())
music = list(map(int, input().split()))

down = 1
up = sum(music)
max_num = max(music)

while down <= up :
    amount = (up + down) // 2
    if amount >=max_num and M >= findAns(amount):
        ans = amount
        up = amount-1
    else: #더 적게 나눠지면, 용량을 줄여야함
        down = amount+1

print(ans)


