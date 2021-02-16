def double(N, res):
    if N <= 1:
        return str(N%2)+res
    return double(int(N/2), str(N%2)+res)


num = int(input())
print(int(double(num, " ")))