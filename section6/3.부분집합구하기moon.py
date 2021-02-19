#N이 주어지면 1~N까지의 원소를 갖는 집합의 부분집합 출력

N = int(input())
arr = [0]*N

def dps(now):
    if now >= N:
        for i in range(0,N):
            if arr[i] == 1:
                print(i+1, end =" ")
        print()

    else:
        arr[now] = 1
        dps(now+1)
        arr[now] = 0
        dps(now+1)


dps(0)
