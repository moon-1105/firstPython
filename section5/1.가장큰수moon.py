import sys
#sys.stdin=open("input.txt", "rt")

N, m = map(str, input().split())
m = int(m)
arr = []
for ch in N:
    arr.append(int(ch))
chk = 0
st = [arr[0]]
not_change = True
for idx in range(1, len(N)):
   # print(arr[idx],"체크")
    while len(st)!=0 and chk < m:
        n = st.pop()
       # print(n,"이랑 비교")
        if arr[idx] <= n:
            st.append(n)
           # print(arr[idx], "넣고 끝냄")
            break
        else:
            chk += 1
            not_change = False
    st.append(arr[idx])

ans = ""
for num in st:
    ans +=str(num)
if not_change:
    print(ans[:-m])
else:
    print(ans)



