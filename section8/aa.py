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
    printMap()
    for m in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                friend[i][j] = min(friend[i][j], friend[i][m] + friend[m][j])
        printMap()


