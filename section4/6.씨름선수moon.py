import sys
#sys.stdin=open("input.txt", "rt")

# N명의 지원자
# 키와 몸무게 중 적어도 하나는 다른사람보다 크거나 무거운 지원자
# 최대 인원

N = int(input())
people = []
for i in range(0,N):
    h, w = map(int, input().split())
    people.append( (h,w) )

#키로 정렬
height = people.copy()
height.sort()
#print(height)

weight = people.copy()
weight.sort( key = lambda x : (x[1], x[0]))
#print(weight)

cnt = 1
for idx in range(0, N-1):
    # 마지막 사람은 키가 젤 클테니 볼 필요 없음
    idx2 = weight.index( (height[idx][0], height[idx][1]))
    # 키가 더 작을 때, 몸무게가 더 많은 사람 있다면, 탈락
    # 키 순서 idx, 몸무게 순서 idx2
    # 몸무게순서가 큰애가 키가 더 크다면 탈락
    chk = True
    for 비교 in range(idx2+1, N):
        if weight[비교][0] > height[idx][0]:
            #print("탈락")
            chk = False
    if chk :
        cnt+=1

print(cnt)
