import sys
from collections import deque

#sys.stdin = open("input.txt","r")

str1 = input()
deq = deque([])

for ch in str1:
    if ch.isdecimal():
        deq.append(int(ch))
    else:
        num1 = deq.pop()
        num2 = deq.pop()
        if ch == "+":
            deq.append(num2+num1)
        elif ch == "-":
            deq.append(num2 - num1)
        elif ch == "*":
            deq.append(num2 * num1)
        elif ch == "/":
            deq.append(num2 / num1)

print(deq.pop())

