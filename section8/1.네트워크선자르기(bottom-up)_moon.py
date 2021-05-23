import sys
sys.stdin = open("in.txt","r")

#네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다
#네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?

if __name__ == "__main__":
    N = int(input())
    L = [0]*N
    L[0], L[1] = 1, 2
    for i in range(2, N):
        L[i] = L[i-1]+L[i-2]

    print(L[N-1])


