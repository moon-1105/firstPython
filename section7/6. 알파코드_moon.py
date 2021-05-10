def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            # code[L]이 알파벳이 딜때마다
            if code[L]==i:
                # 결과에 추가함.
                res[P]=i
                # 추가되면 다 다음 인덱스 확인
                DFS(L+1, P+1)
            # 0이 포함되는지 여부는 이렇게 체크함.
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                # 0이 포함되면 (10의배수면)
                res[P]=i # 바로 넣어버리고
                DFS(L+2, P+1) # L+1 까지 봤으니까 다음걸로 넘김???

if __name__=="__main__":
    code=list(map(int, input()))
    n=len(code)
    code.insert(n, -1)
    res=[0]*(n+3)
    cnt=0
    DFS(0, 0)
    print(cnt)