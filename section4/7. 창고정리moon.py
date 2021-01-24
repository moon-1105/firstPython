import sys
# 높이조정 => 가장 높은 곳의 상자를 가장 낮은 곳으로
# m회 조정한 후, 차이를 출
#sys.stdin=open("input.txt", "rt")

L = int(input())
box = list(map(int, input().split()))
M = int(input())

box.sort()

# 높이 조절
for 횟수 in range(0, M):
    box[0] += 1
    box[L-1] -= 1
    box.sort()

print(box[L-1]-box[0])