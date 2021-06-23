import sys
sys.stdin = open("in.txt")

def printMap():
    for ele in friend:
        for e in ele[1:] :
            if e == 5000:
                print('n',end=" ")
            else:
                print(e,end=" ")
        print()
    print()
if __name__ == "__main__":
    N = int(input())
    friend = []
    for _ in range(N+1):
        friend.append([5000]*(N+1))

    while(True):
        i, j = map(int, input().split())
        if i==-1 and j==-1:
            break
        friend[i][j] = 1
        friend[j][i] = 1

    for m in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                friend[i][j] = min(friend[i][j], friend[i][m] + friend[m][j])
                friend[j][i] = friend[i][j]
    #printMap()

    result = [0]*(N+1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            result[i] = max(result[i], friend[i][j])
    print(result)
    target = min(result)

    ans=[]
    for idx in range(len(result)):
        if result[idx] == target:
            ans.append(idx)
    if len(ans) >=2:
        for i in range(2):
            print(ans[i], end=" ")
    else:
        for a in ans:
            print(a, end=" ")
    print()
    for a in ans:
        print(a, end=" ")
