import sys
#sys.stdin=open("in.txt", "r")
def dps(i, sum, tsum):
    if sum > C:
        return
    if i >= N:
        global result
        if result < sum:
            result = sum
        return
    dps(i+1, sum+dogs[i], tsum+dogs[i])
    dps(i+1, sum, tsum + dogs[i])

C = 259
N = 5
dogs = [81,58,42,33,61]
#for _ in range(0,N):
#    dogs.append(int(input()))

result = 0
dps(0,0,0)
print(result)






