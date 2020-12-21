def makeScore(score):
    dice = [0]*7
    for i in score:
        dice[i] = dice[i]+1
    award = 0
    if 3 in dice:
        award = 10000 + dice.index(3)*1000
    elif 2 in dice:
        award = 1000 + dice.index(2)*100
    else:
        for num in range(6,1,-1):
            if dice[num] == 1:
                award = num*100
    return award
    
    
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

max = -1
for score in arr:
    tmp = makeScore(score)
    if max < tmp:
        max = tmp
print(max)
