import sys
#sys.stdin=open("input.txt", "r")
from collections import deque

#접수한대로 제일 앞에있는 목록 꺼냄
# 나머지에서 더 위험하면 뒤로 보냄

class pat:
    def __init__(self, num, risk):
        self.num = num
        self.risk = risk
    def __str__(self):
        return str(self.num)+"번째 환자:"+str(self.risk)
    def __repr__(self):
        return str(self.num) + "번째 환자:" + str(self.risk)

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
# M번째 환자는 몇번째로 진료를 받는가?
patients = []
idx = 0
for r in tmp:
    A = pat(idx, r)
    patients.append(A)
    idx+=1
patients = deque(patients)
find = patients[M]
def canHeal(now):
    for p in patients:
        if now.risk < p.risk:
            return False
    return True

heal = []
while patients:
    now = patients.popleft()
    if canHeal(now):
        heal.append(now)
    else:
        patients.append(now)
#print(patients)
#print(heal)

print(heal.index(find)+1)

"""
수업 메모
Q = [(pos, val) for pos, val in enumerate(list(map, input().split()))]
enumerate 안의 리스트 까지 입력 받아서 리스트
자동으로 pos에 index 넣어서 채크해줌
"""