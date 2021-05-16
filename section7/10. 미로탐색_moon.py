#미로를 탈출하는 경로의 가지수를 출력
import sys
sys.stdin = open("in.txt","r")

dir = [[1,0],[0,1],[-1,0],[0,-1]]
def isOkay(next, his):
    if 0<= next[0] <7 and 0<= next[1] <7:
        if his[next[0]][next[1]] == 0 :
            if maze[next[0]][next[1]] == 0:
                return True
    return False

count = 0
def cal(st, his):
    global count
    now = st.pop()
    if now == [6, 6]:
        count+=1
    else:
        for d in dir:
            next = [now[0]+d[0],now[1]+d[1]]
            if isOkay(next, his):
                st.append(next)
                his[next[0]][next[1]] = 1
                cal(st, his)
                his[next[0]][next[1]] = 0


if __name__ == "__main__":
    maze = []
    his  = []
    for _ in range(7):
        maze.append(list(map(int, input().split())))
        his.append([0,0,0,0,0,0,0])
    st = [[0,0]]
    his[0][0] = 1
    cal(st, his)
    print(count)