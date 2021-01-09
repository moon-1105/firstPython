import sys
#sys.stdin=open("input.txt", "rt")
def 나누기(arr, 시도):
    cnt = 0
    for 길이 in arr:
        cnt+= 길이 // 시도
    #print(시도, "만큼 자르면 =>", cnt, "개")
    return cnt

K, N = map(int, input().split())
arr = []
for i in range(0,K):
    arr.append(int(input()))

# K 개의 전선으로, N개의 전선을 만드려고 할때 그 길이는 ?
sum = 0
for 길이 in arr:
    sum += 길이

시도 = int(sum/N)
시도_max = int(sum/N)
시도_min = int(sum/N)
가능 = 0
dup_check = -1
dup = False
while 1:
    dup_check = 시도
    가능 = 나누기(arr, 시도)
    if(가능== N):
        #print("조각 수가 같으나, 더 크게 잘라도 괜찮은지 검사해야함")
        시도 += 1
        tmp = 나누기(arr, 시도)
        while tmp == N:
            시도 += 1
            tmp = 나누기(arr, 시도)
        break
    elif 가능 > N:
        #print("더 잘게 잘라졌으므로, 더 크게 자름")
        시도_min = 시도
        시도 = int((시도_max+시도_min)/2)
    else:
        #print("조각이 더 적으므로, 더 작게 자름")
        시도_max = 시도
        시도_min = int(시도/2)
        시도 = int(시도/2)
    if(dup_check == 시도):
        dup = True
        break

if dup:
    print(시도)
else:
    print(시도-1)









