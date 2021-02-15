import sys
from collections import deque

#알파벳과 개수가 일치하면 아나그램
#아나그램인지 아닌지 판별

word1 = input()
word2 = input()

chk1=[0]*100
chk2=[0]*100

for ch in word1:
    chk1[ ord(ch)-65 ]+=1

for ch in word2:
    chk2[ ord(ch)-65 ]+=1

#print(chk1)
#print(chk2)



if chk1 == chk2:
    print("YES")
else:
    print("NO")
