import sys
#sys.stdin=open("in.txt", "r")
#양팔저울을 한번만 이용해서 원하는 물의 무게를 그릇에 담고자 한다.
# K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는
# 몇 가지가 있는 지 출력하는 프로그램
K = int(input())
chu = list(map(int, input().split()))
limit = sum(chu)
res = set() # 아예 중복을 없앰.
def cal(idx, sum):
    global res
    if idx >= K:
        if 0< sum <= limit:
            # set으로 설정해서 아예 중복을 없앰.
            res.add(sum)
    else:
        # 경우의 수 말고,
        # 합가지고만 하니까 경우의 수 고려를 막 넣었다 뻇다 할필요가 없어짐.
        cal(idx+1, sum - chu[idx])
        cal(idx+1, sum)
        cal(idx+1, sum + chu[idx])


cal(0,0)
"""
cnt =0
for idx in range(1, limit+1):
    if idx not in res:
        cnt+=1
print(cnt)
"""
print(limit-len(res))


