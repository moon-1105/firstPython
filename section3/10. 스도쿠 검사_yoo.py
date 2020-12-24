import sys
import math
#sys.stdin=open("in2.txt", "rt")

arr = [[int(x) for x in input().split()]for y in range(9)]
arr1 = [[False for x in range(9)] for y in range(27)]
c, d = 0, 0
for i in range(0, 9):
    for j in range(0, 9):
        c, d = 0, 0
        if not arr1[i][arr[i][j]-1]:
            arr1[i][arr[i][j]-1] = True
        else:
            print('NO')
            sys.exit()
        if not arr1[i+9][arr[j][i]-1]:
            arr1[i+9][arr[j][i]-1] = True
        else:
            print('NO')
            sys.exit()
        c = i // 3
        d = (j // 3) * 3
        if not arr1[18 + c + d][arr[i][j]-1]:
            arr1[18 + c + d][arr[i][j]-1] = True
        else:
            print('NO')
            sys.exit()
print('YES')
