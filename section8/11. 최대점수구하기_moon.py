import sys
#sys.stdin = open("in.txt","r")
"""
정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 합니다. 
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다. 
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다.
"""

if __name__ == "__main__":
    N, time = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        # [점수, 푸는시간]

    ans = [0]*(time+1)
    # ans[i] 는 i 분이 지났을 때 얻을 수 있는 최대점수
    for ele in arr:
        for i in range(time, ele[1]-1, -1):
            ans[i] = max(ans[i-ele[1]] + ele[0], ans[i])
        #print(ans)
    print(ans[time])
