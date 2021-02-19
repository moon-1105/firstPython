N = int(input())
arr = list(map(int, input().split()))
chk = [0]*N
flag = False

def dps(now):
    if now >= N:
        #여기서 2개 체크
        sum1, sum2 = 0, 0
        for i in range(0, N):
            if chk[i] == 1:
                sum1+=arr[i]
            elif chk[i] == 2:
                sum2+=arr[i]
        if sum1==sum2:
            #print("YES")
            global flag 
            flag = True
            return True
        else:
            #print("NO")
            return False
    else:
        chk[now] = 1
        dps(now+1)
        chk[now] = 2
        dps(now+1)


dps(0)
if flag:
    print("YES")
else:
    print("NO")
