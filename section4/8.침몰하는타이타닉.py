import sys
#sys.stdin=open("input.txt", "rt")
#구명보트 2명 이하 무게 M 이하
#모두가 탈출하기위한 구명보트의 최소개수

N, M = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort(reverse=True)

midx = N-1
cnt = 0
for idx in range (0, N):
    if weight[idx] == -1 :
        continue
    elif weight[idx] + weight[midx] <= M:
        #print(weight[idx],", ",weight[midx],"보트 탔다")
        weight[midx] = -1
        midx -= 1
        cnt+=1
    else:
        #print(weight[idx],"보트 탔다")
        cnt+=1

print(cnt)
