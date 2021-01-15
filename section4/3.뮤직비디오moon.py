import sys
#sys.stdin=open("input.txt", "rt")
# 노래의 순서가 바뀌면 안됨.!!!
# M개에 다 녹음이 가능한데, DVD의 크기를 최소로해야함.

def find용량(music, 용량):
    개수 = 0
    tmp = 0
    for 곡 in music :
        #print(개수,"개 째, 지금",tmp,"까지 사용함",곡,"체크",end="")
        if 곡+tmp < 용량:
            tmp += 곡
            # 여기서 같은거 체크하고, 같다면 개수+1 크기 0 했었음. 그러니까 크기가 2일때 1 은 2개넣어도 되고 1개 넣어도 되는데
            # 반드시 2개를 넣게되어 별로임..개수 정해져있으므로 크기가 최소여야하므로,,
        else:
            tmp=곡
            개수 += 1
    return 개수

N, M = map(int, input().split())
music = list(map(int, input().split()))

용량 = sum(music)
up = sum(music)
down = max(music)
tmp = 0

while tmp != M :
    tmp = find용량(music, 용량)
    if tmp == M:
        break
    #print(용량,"크기에 개수 : ",tmp)
    #여기서 이분탐색을 하려고 했더니 잘안됨. 하나씩 함.
    if tmp > M: # 더 잘게 나눠지면, 용량을 키워야함
        용량 +=1
    else: #더 적게 나눠지면, 용량을 줄여야함
        용량 -= 1

print(용량)
# 1일때 안나오는거랑 용량 더 큰거 체크하는거


