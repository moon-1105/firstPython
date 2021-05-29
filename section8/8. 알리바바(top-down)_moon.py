import sys
#sys.stdin = open("in.txt","r")

if __name__ == "__main__":
    N = int(input())
    stone = []
    ans = []
    for _ in range(N):
        stone.append(list(map(int, input().split())))
        ans.append([0]*N)

    ans[N-1][N-1] = stone[N-1][N-1]
    for i in range(N-2,-1,-1):
        ans[N-1][i] = stone[N-1][i]+ans[N-1][i+1]
        ans[i][N - 1] = stone[i][N-1] + ans[i+1][N - 1]

    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            right = ans[i][j+1]
            under = ans[i+1][j]
            if right > under:
                ans[i][j] = stone[i][j] + under
            else:
                ans[i][j] = stone[i][j] + right

    print(ans[0][0])


