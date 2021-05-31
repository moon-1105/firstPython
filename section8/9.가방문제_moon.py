import sys
sys.stdin = open("in.txt","r")
"""
이 보석을 가방에 담는데 XX kg를 넘지 않으면서 
최대의 가치가 되도록 하려면 어떻게 담아야 할까요?
"""
class jewel:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def __str__(self):
        return "가치:"+str(self.value)+" / "+"무게: "+str(self.weight)

if __name__ == "__init__":
    N, limit = map(int, input().split())
    arr = []
    for _ in range(N):
        w, v = map(int, input().split())
        arr.append(jewel(v, w))
    ans = [0]*N
    ans[0] = max(arr)
    for i in range(0,N)



