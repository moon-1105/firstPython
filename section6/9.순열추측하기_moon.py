# N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램

N, F = map(int, input().split())
#N, F = 4, 16

num = []
for i in range(1, N+1):
    num.append(i)

stop = False
#순열구하기
def cal(arr):
    global stop
    if stop == True:
        ans = arr
        return
    if len(arr) == N:
        #print(arr)
        #답인지 체크하기
        if check(arr) == F:
            stop = True
            for ele in arr:
                print(ele, end=" ")
            return

    for n in num:
        if not n in arr:
            arr.append(n)
            cal(arr)
            arr.pop()

"""
4=> 1, 3, 3, 1
5=> 1, 4, 6, 4, 1
6=> 1, 5, 10, 10, 5, 1
"""
def check(arr):
    sum = 0
    sum += arr[0]
    sum += arr[N-1]
    if N%2==0: #짝수면
        for i in range(1, N - 1):
            sum += arr[i] * (N / 2 - i)

    else: #홀수면
    #print(sum)
    return sum


cal([])
