import sys
#sys.stdin=open("in.txt", "r")
N = int(input())
take = []
pay = []
# 걸리는 일 수 T, 받을 수 있는 금액 P
for _ in range(0,N):
    tmp = list(map(int, input().split()))
    take.append(tmp[0])
    pay.append(tmp[1])

maxMoney = 0
def f_cal(money, day, arr):
    global maxMoney
    if day == N:
       # print(arr, money)
        if maxMoney < money:
            maxMoney = money
        return
    if day > N:
        return
    arr.append(day)
    f_cal(money+pay[day], day+take[day], arr)
    arr.pop()
    f_cal(money, day + 1, arr)

f_cal(0,0,[])
print(maxMoney)


