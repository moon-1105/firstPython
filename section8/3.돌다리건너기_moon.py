
if __name__ == "__main__":
    N = int(input())
    stone = [0]*(N+2)
    stone[1] = 1
    stone[2] = 2
    for i in range(3, N+2):
        stone[i] = stone[i-1] + stone[i-2]
    print(stone[N+1])