import sys
from collections import deque

#sys.stdin = open("in5.txt","r")

# 시쓰기 전에 단어 적어둠.
# 그중 안쓴 단어가 무엇인지 찾기.

N = int(input())
word = []
for _ in range(0,N):
    word.append( input() )

word = set(word)
word = list(word)

count = [0]*N

test = []
for _ in range(0,N-1):
    test.append( input() )

for w in test:
    idx = word.index(w)
    if idx >= 0 :
        count[idx]+=1

for i in range(0,N):
    if count[i] ==0:
        print(word[i])
        break
