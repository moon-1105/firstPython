"""
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두
출력합니다.
"""
"""
N, M = map(int, input().split())
"""
N, M = 5, 3
marv = []
for num in range(1, N+1):
    marv.append(num)
ans_arr = []

def cal(arr, idx, m_idx, 개수):
    if M == 개수:
        # 답인 경우
        newArr = arr[:]
        global ans_arr
        ans_arr.append(newArr)
        #print(arr)
        return
    if  idx >= M or m_idx >= N or M < 개수:
        return
    arr[idx]= marv[m_idx]
    cal(arr, idx+1, m_idx+1, 개수+1)
    cal(arr, idx, m_idx+1, 개수)

cal([0]*M,0,0,0)
