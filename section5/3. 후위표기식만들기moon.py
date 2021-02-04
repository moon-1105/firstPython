import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(': # 우선 넣기
            stack.append(x)
        elif x=='*' or x=='/': #기호가나오면 다음 기호가 나오기 전까지 모두 빼서
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop() # 한데 뭉쳐서
            stack.append(x) #넣기
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')': # 괄호가나오면
            while stack and stack[-1]!='(': #다음 괄호가 나올때까지
                res+=stack.pop() #한데 뭉쳐서 결과에 넣기
            stack.pop() #그리고 하나 빼버림 (
while stack:
    res+=stack.pop()
print(res)
