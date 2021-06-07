import sys
#sys.stdin = open("in.txt","r")
"""
이 보석을 가방에 담는데 XX kg를 넘지 않으면서 
최대의 가치가 되도록 하려면 어떻게 담아야 할까요?
"""

if __name__ == "__main__":
    N, limit = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list( map(int, input().split())))
    """
    ans[i] 에는 i kg 까지 담았을 때의 최대의 가치
    무게별로 체크해가면서 최대의 가치를 체크. 
    """
    ans = [0] * (limit+1)
    for ele in arr:
        무게, 가치 = ele[0], ele[1]
        for i in range(무게, limit+1):
            if ans[i] < ans[i-무게] + 가치:
                ans[i] = ans[i-무게] + 가치
        #print("무게:",무게, ans)

    print(max(ans))






