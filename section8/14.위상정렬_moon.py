import sys
sys.stdin = open("in.txt")

"""
위상정렬은 어떤 일을 하는 순서를 찾는 알고리즘입니다.
각각의 일의 선후관계가 복잡하게 얽혀있을 때 각각 일의 선후관계를 유지하면서 전체 일의
순서를 짜는 알고리즘입니다.
만약 아래와 같은 일의 순서를 각각 지키면서 전체 일의 순서를 정한다면
"""

if __name__=="__main__":
    N, M = map(int, input().split())
    chart = [[0]*N]
    for _ in range(M):
        i, j = map(int, input().split())
        chart[i][j] =
