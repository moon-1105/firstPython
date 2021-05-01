
N, M = map(int, input().split())
#N, M = 4, 2
# N까지 번호가 적힌 구슬, 이중에 M 개를 뽑는 방법의 수

marvel =[]
for i in range(1, N+1):
    marvel.append(i)
count = 0
def cal(arr, idx):
    if M == len(arr):
        global count
        count += 1
        for ele in arr:
            print(ele, end=" ")
        print()
        return
    if idx >= N:
        return
    arr.append( marvel[idx] )
    cal(arr, idx+1)
    arr.pop()
    cal(arr, idx+1)

arr = []
cal(arr, 0)
print(count)


