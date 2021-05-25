import sys
"""
N개의 자연수로 이루어진 수열이 주어졌을 때, 
그 중에서 가장 길게 증가하는(작은 수에서 큰수로) 원소들의 집합을 찾는 프로그램을 작성하라.
"""
#sys.stdin = open("in.txt","r")
# 자기 보다 값이 작은 것 중에 ans 가 가장 많은 것을 고름
def cal(idx):
    #print(rest)
    maxV = 0
    if arr[idx] < min(rest):
        return 1
    else:
        for jdx in range(0, len(rest)):
            if arr[jdx] < arr[idx]:
                if ans[jdx] > maxV:
                    maxV = ans[jdx]

        return maxV+1

if __name__=="__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    ans = [0]*N
    rest = []
    ans[0] = 1
    if arr[0] < arr[1]:
        ans[1] = 2
    else:
        ans[1] = 1
    rest.append(arr[0])
    rest.append(arr[1])

    for idx in range(2, N):
        ans[idx] = cal(idx)
        rest.append(arr[idx])
        #print(ans)
    print(max(ans))

