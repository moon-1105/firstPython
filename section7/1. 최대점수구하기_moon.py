def sumTime(arr):
    sum=0
    for ele in arr:
        sum += ele[1]
    return sum
def sumScore(arr):
    sum=0
    for ele in arr:
        sum += ele[0]
    return sum
"""
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록
"""
N, M = map(int, input().split()) #5, 20 #
ques = []
for _ in range(0,N):
  tmp = list(map(int, input().split()))
  ques.append(tmp)

#ques = [[10,5],[25,12],[15,8],[6,3],[7,4]]
bestScore = 0
def maxScore(arr, idx, limit):
    global bestScore
    if limit == len(arr):
        nowTotalTime = sumTime(arr)
        if nowTotalTime <= M:
            tmp = sumScore(arr)
            if bestScore < tmp:
                bestScore = tmp
        return
    if idx >= N:
        return
    arr.append(ques[idx])
    maxScore(arr, idx+1, limit)
    arr.pop()
    maxScore(arr, idx+1, limit)


for limit in range(N, 1, -1):
    maxScore([],0, limit)

print(bestScore)