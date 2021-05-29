import sys
sys.stdin = open("in.txt","r")
"""
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다. 탑은 벽돌을 한 개씩 아래
에서 위로 쌓으면서 만들어 간다. 아래의 조건을 만족하면서 가장 높은 탑

밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다
무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다
"""

class block:
    def __init__(self, w, h, wei):
        self.w = w
        self.h = h
        self.wei = wei

    def __str__(self):
        return "벽돌 " +str(self.w)+"*"+str(self.h) +"/" + str(self.wei) +"kg"
def canUp(b1, b2):
    if b1.w >= b2.w :
        if b1.wei >= b2.wei:
            return True
    return False

def cal(idx):
    poss = []
    print(blocks[idx], end="=> ")
    for j in range(idx-1, -1, -1):
        if canUp(blocks[j], blocks[idx]):
            print(blocks[j], end=", ")
            poss.append(ans[j])
    print()
    if len(poss) == 0 :
        return blocks[idx].h
    else:
        return blocks[idx].h + max(poss)

if __name__ == "__main__":
    N = int(input())
    blocks= []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        blocks.append(block(tmp[0], tmp[1], tmp[2]))

    ans = [0]*N
    ans[0] = blocks[0].h

    if canUp(blocks[0], blocks[1]):
        ans[1] = ans[0] + blocks[1].h
    else:
        ans[1] = blocks[1].h

    for i in range(2, N):
        ans[i] = cal(i)

    print(ans)
