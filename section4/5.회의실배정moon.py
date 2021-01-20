import sys
#sys.stdin=open("input.txt", "rt")

# 1개의 회의실이 있는데, 이를 사용하려는 n개의 회의들에 대해서 시간표 구성
# 안겹치게 회의실 사용할 수 있는 최대수의 회의
# 끝나는 시간을 기준으로 선택하려 했는데 잘 안되었음
# 그리디 => 정렬해서 채워넣기

n = int(input())
회의 = []
for i in range(0,n):
    s, e = map(int, input().split())
    회의.append((s,e))

회의.sort(key = lambda x : (x[1], x[0]))
# x[1], x[0] 순으로 우선순위를 두고 정렬할 것
# 그냥 sort 하면, 순서대로 0, 1 기준으로 정렬됨.
#print(회의)
endTime = 0
cnt = 0
for s, e in 회의:
    if s >= endTime:
        endTime = e
        cnt+=1

print(cnt)





