import sys
import math

#sys.stdin = open("in4.txt", "rt")

def Hu(arr):
    tmp = []
    i = 0
    check = 0
    while len(arr) > 1:
        if arr[i] == '(':
            c = 1
            while arr[i + c] != ')':
                tmp.append(arr[i + c])
                c += 1
            tmp1 = arr[:i]
            tmp2 = Hu(tmp)
            tmp1.append(tmp2)
            arr = tmp1 + arr[i + c + 1:]
            arr[0] = Hu(arr)
            break
        if (arr[i] == '*' or arr[i] == '/') and check == 1:
            tmp = arr[i - 1] + arr[i + 1] + arr[i]
            tmp1 = arr[:i - 1]
            tmp1.append(tmp)
            arr = tmp1 + arr[i + 2:]
            arr[0] = Hu(arr)
            break
        if (arr[i] == '+' or arr[i] == '-') and check == 2:
            tmp = arr[i - 1] + arr[i + 1] + arr[i]
            tmp1 = arr[:i - 1]
            tmp1.append(tmp)
            arr = tmp1 + arr[i + 2:]
            arr[0] = Hu(arr)
            break
        i += 1
        if i == len(arr):
            i = 0
            check += 1
    return arr[0]

N = str(input())
N = list(map(str, N))
answer = Hu(N)
print(answer)
