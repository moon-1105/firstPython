import sys
sys.stdin=open("input.txt", "rt")

#마굿간 정하기
def chk_ans(dis):
    if len(좌표)== 2:
        return max(좌표)-1
    cnt = 1
    pre = 좌표[0]
    for idx in range(1, len(좌표)):
        if 좌표[idx] - pre >= dis:
            pre = 좌표[idx]
            cnt+=1
    return cnt

N, C = map(int, input().split())
좌표 = []
for i in range(0,N):
    좌표.append(int(input()))
좌표.sort()
#말들끼리 최대한 멀리 두었을 때, 가장 가까운 두 말의 최대 거리
#거리는 최소 1부터 max(마굿간좌표)까지 될 수 있음.
up, down =  max(좌표), min(좌표)
ans = 0

while up >= down :
    mid = (up + down) // 2
    # 그 거리가 답이라면, 해당 거리 미만의 간격의 좌표는 답이 될 수 없음.
    chk = chk_ans(mid)
    # 거리 이상의 좌표에만 말을 두고나서, 그 말의 총 개수가 C와 같다면그 거리가 답임.
    #print(mid,"거리일때 말이",chk,"개 들어간다 =>",up, down)

    if chk >= C: # 말 개수가 더 많거나 같다면, 거리를 늘여야함(최대 거리니까)
        ans = mid
        down = mid + 1
    else: # 말 개수가 더 적다면, 거리를 좁혀야함

        up = mid - 1

print(ans)
