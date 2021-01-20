
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_two(num, answer):
    if num > 1:
        answer = str(num % 2)
        num = num // 2
    if not num == 1:
        answer = f_two(num, answer) + answer
    else:
        answer = str(1) + answer
    return answer
N = int(input())
answer = ""
print(f_two(N, answer))
