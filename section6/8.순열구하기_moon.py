"""
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두
출력합니다.
"""

N, M = map(int, input().split())
"""
N, M = 3, 2
"""
marv = []
for num in range(1, N+1):
    marv.append(num)
ans_arr = []
lastNum = 0
def cal(arr):
    if M == len(arr):
        # 답인 경우
        for ele in arr:
            print(ele, end=" ")
        global lastNum
        lastNum+=1
        print()
        return
    for num in range(1, N+1):
        if not(num in arr):
            arr.append(num)
            cal(arr)
            arr.pop()

for num in range(1, N+1):
    startArr = [ num ]
    cal(startArr)

print(lastNum)