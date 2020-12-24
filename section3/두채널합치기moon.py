import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr=arr1+arr2
arr.sort()

for ch in arr:
    print(ch, end=" ")

