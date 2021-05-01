"""
N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수
는 몇 개가 있는지 출력
"""
N, K = map(int, input().split())
arr = list(map(int, input().split()))
M = int(input())

#N, K, M = 5,3,6
#arr = [2, 4, 5, 8, 12]

cnt = 0
def cal(ans, idx):
    global cnt
    if K == len(ans):
        if sum(ans) % M == 0 :
            cnt += 1
        return
    if idx >= N :
        return
    ans.append(arr[idx])
    cal(ans, idx+1)
    ans.pop()
    cal(ans, idx+1)

cal([], 0)
print(cnt)
