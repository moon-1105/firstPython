import sys

def cal(N):
    if stair[N] != 0 :
        return stair[N]
    if N==1 or N==2:
        return stair[N]
    cal(N-1)
    cal(N-2)
    stair[N] = stair[N-1]+stair[N-2]

if __name__ == "__main__":
    N = int(input())
    stair = [0]*(N+1)
    stair[1], stair[2] = 1, 2
    cal(N)
    print(stair[N])