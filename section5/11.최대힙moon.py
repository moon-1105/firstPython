import heapq
maxheap = []
num = int(input())

while num != -1:
    if num == 0:
        if len(maxheap) == 0:
            print(-1)
        else:
            print(heapq.heappop(maxheap)[1])

    else:
        heapq.heappush(maxheap, (-num, num))
    # 새로
    num = int(input())
