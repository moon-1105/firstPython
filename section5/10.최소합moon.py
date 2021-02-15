import heapq

# 최소힙
heap = []

num = int(input())

while num != -1:
    if num == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, num)
    # 새로
    num = int(input())
