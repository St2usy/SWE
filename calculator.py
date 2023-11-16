# 이스터에그 함수, 특정한 숫자일 때 특별한 메시지 출력
def egg_messages(num):
    if num == 7:
        print("행운")
    elif num == 1221:
        print("종강종강 돌을 던지자")
    elif num == 18:
        print("바른말고운말")
    elif num == 0:
        print("0은 여기서 False란다")
    elif num == 1:
        print("1은 여기서 True란다")
    elif num == 2:
        print("Binary..?")
    elif num == 534:
        print("컴공생들의 무덤")


error = 0
first_operand = 0

try:
    first_operand = int(input())  # 첫번째 피연산자 입력
    egg_messages(first_operand)  # 특정한 숫자인 경우 메시지 출력
except ValueError:
    error += 1

operator = input()  # 연산자 입력

# 연산자가 '='이 나오기 전까지 연산을 반복
while operator != '=':
    try:
        next_operand = int(input())
        egg_messages(next_operand)
    except ValueError:
        error += 1

    # 지원되는 연산자인지 확인 후 계산 수행
    if operator == '+':
        first_operand += next_operand
    elif operator == '-':
        first_operand -= next_operand
    elif operator == '*':
        first_operand *= next_operand
    else:
        error += 1  # 잘못된 연산자가 입력된 경우 에러 카운트 증가

    next_operator = input()  # 다음 연산자 입력


    if operator != next_operator :  # 동일한 연산인지 확인
        operator = next_operator
        if operator != '=':
            error += 1

if error > 0:
    print("ERROR!")  # 에러가 발생했을 때 "ERROR!" 출력
else:
    print(first_operand)  # 계산 결과 출력
