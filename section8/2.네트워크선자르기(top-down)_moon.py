import sys
#sys.stdin = open("in.txt", "r")

def cal(N):
    if L[N]!=0:
        return L[N]
    if N == 1 or N == 2:
        return L[N]
    else:
        cal(N-1)
        cal(N - 2)
        L[N] = L[N - 1] + L[N - 2]

if __name__ == "__main__":
    N = int(input())
    L = [0]*(N+1)
    L[1] = 1
    L[2] = 2
    cal(N)
    print(L[N])