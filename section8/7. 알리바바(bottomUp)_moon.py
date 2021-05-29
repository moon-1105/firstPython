import sys
#sys.stdin = open("in.txt","r")

"""
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다.
즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
에너지의 최소량
"""

if __name__ == "__main__":
    N = int(input())
    stone = []
    ans = []
    for _ in range(N):
        stone.append(list(map(int, input().split())))
        ans.append([0]*N)
    ans[0][0] = stone[0][1]
    for i in range(N):
        ans[0][i] = ans[0][i-1] + stone[0][i]
        ans[i][0] = ans[i-1][0] + stone[i][0]

    for i in range(1, N):
        for j in range(1, N):
            up = ans[i-1][j]
            left = ans[i][j-1]
            if up < left:
                ans[i][j] = up + stone[i][j]
            else:
                ans[i][j] = left + stone[i][j]

    #for ele in ans:
    #    print(ele)
    print(ans[N-1][N-1])