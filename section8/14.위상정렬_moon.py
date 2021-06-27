import sys
sys.stdin = open("in.txt")

"""
위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘입니다.
각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의
순서를 짜는 알고리즘입니다.
만약 아래와 같은 일의 순서를 각각 지키면서 전체 일의 순서를 정한다면
"""
def printMap():
    for idx in range(1, N+1):
        for jdx in range(1, N+1):
            print(chart[idx][jdx], end=" ")
        print()

if __name__=="__main__":
    N, M = map(int, input().split())
    chart = []
    for _ in range(N+1):
        chart.append([0]*(N+1))
    print(chart)
    for _ in range(M):
        i, j = map(int, input().split())
        chart[i][j] = 1
    # 전체적으로 그래프를 한번씩 돌면서 계속 업데이트 해야함.
    # 갈수있는걸(겹쳐서라도) 전부 1 체크 /
