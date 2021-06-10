import sys
sys.stdin = open("in.txt")
"""
모든 도시에서 모든 도시로 이동하는데 쓰이는 비용의 최소값
"""
if __name__ == "__main__":
    city, road = map(int, input().split())
    arr = []
    ans = []
    for _ in range(road):
        arr.append(list(map(int, input().split())))
        # [도시1, 도시2, 비용]
        ans.append([0]*city)q


