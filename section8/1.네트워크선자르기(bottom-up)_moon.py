import sys
#sys.stdin = open("in.txt","r")

#네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다
#네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?

cnt = 0
def cal(total):
    global cnt
    if total >= N:
        if total > N:
            return
        else:
          #  print("성공")
            cnt+=1
            return
    cal(total+1)
    cal(total+2)

if __name__ == "__main__":
    N = int(input())
    cal(0)
    print(cnt)


