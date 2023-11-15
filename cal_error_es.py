
error = 0  
try:
    x = int(input()) #정수로 입력 받음 정수가 아닐 시 error 출력 
except ValueError:
    x = 0
    error += 1

op = input() #op는 연산자

while(op!='='): #연산자가 =이 나오기전까지 반복연산
    try:
        y = int(input())
    except ValueError:
        y = 0
        error += 1

    if (op == '+'): 
        x += y 
    elif (op == '-'): 
        x -= y 
    elif (op == '*'): 
        x *= y 
    else:
        error += 1 #더하기, 빼기, 곱하기 연산자 이외의 것일 경우 error 출력
    op2 = input() # 다음 연산자 입력
    if (op != op2): # 동일한 연산인지 확인
        op = op2
        if (op != '='):
            error += 1
print(x) #출력


if (error > 0):
    print("ERROR!")
else:
    print(x)
