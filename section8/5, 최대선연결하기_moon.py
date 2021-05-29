import sys
#sys.stdin = open("in.txt","r")

def cal(num):
    possible=[]
    기준 = right.index(num)
   # print(num,"체크")
    # 해당 숫자보다 작은 애들을 하나씩 검사
    for j in range(num-1, 0, -1):
        if right.index(j) < 기준:
          #  print("연결가능", j, right.index(j))
            possible.append( ans[j] )
        #else:
         #   print("연결안됨", j, right.index(j))

    if len(possible) == 0 :
        #print("가능한게 없음")
        return 1
    return max(possible)+1


if __name__ == "__main__":
    N = int(input())
    right = list(map(int, input().split()))
    # 자기숫자의 right 인덱스보다 크면 out 작으면 ok 그 답+1
    ans = [0]*(N+1)
    ans[1] = 1
    if right.index(1) > right.index(2):
        ans[2] = 1
    else:
        ans[2] = 2
    for i in range(3, N+1):
        ans[i] = cal(i)

    #print(ans)
    print(max(ans))