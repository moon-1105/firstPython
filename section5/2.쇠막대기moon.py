import sys
#sys.stdin = open("input.txt","r")

# 잘려진 쇠막대기 조각 개수를 구하라
# ()은 레이저
tmp = input()
arr = []
for ch in tmp:
    arr.append(ch)
#print(arr)
st = []
laser = 0
dir = "left"
ans = 0
for chk in arr:
    if chk == '(':
        st.append(chk)
        laser+=1
        dir = "left"
    else:
        laser -=1
        if dir == "left":
            ans += laser
        else:
            ans += 1
        st.pop()
        dir = "right"

print(ans)
