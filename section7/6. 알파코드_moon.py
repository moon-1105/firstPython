import sys
#sys.stdin=open("in.txt", "r")

tmp = input()
num = []
for ch in tmp:
    num.append(ch)

N = len(num)
word = set()
def cal(idx, w):
    global word
    if idx == N:
        if w[len(w)-1] =='/':
            w=w[:-1]
        word.add(w)
        return
    else:
        tmpw = list(w.split('/'))
        if int(tmpw[len(tmpw)-1]+num[idx]) > 26:
            # 여기서 끝내기
            cal(idx, w+'/')
        else:
            w += num[idx]
            # 여기서 끝내지 않기
            cal(idx+1, w)
            # 여기서 끝내기
            cal(idx+1,w+'/')
cal(0, '')
#print(word)
_ans = []
for ele in word:
    _ans.append( list(map(int, ele.split('/'))))
#print(_ans)
word=[]
ch=''
for case in _ans:
    for ele in case:
        ch += chr(ele+64)
    word.append(ch)
    ch=''
word.sort()
#print(word)

for w in word:
    print(w)
print(len(word))


