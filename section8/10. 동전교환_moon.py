import sys
#sys.stdin = open("in.txt","r")
"""
거스름돈을 가장 적은 수의 동전으로 교환
해주려면 어떻게 주면 되는가?
"""
if __name__ == "__main__":
    N = int(input())
    coin = list(map(int, input().split()))
    limit = int(input())
    # ans[i] i의 값에서 가장 적은 수의 동전
    ans = [1000000]*(limit+1)
    coin.sort()
    for i in range(0, min(coin)):
        ans[i] = 0

    for c in coin:
        ans[c] = 1
        for i in range(c+1, limit+1):
            if ans[i] > ans[i-c]+ c//c:
                ans[i] = ans[i-c]+ c//c
        #print(c ,"-> ",ans)
    print(ans[limit])
