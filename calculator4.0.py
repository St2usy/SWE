class calculator:
    def __init__(self):
        self.__errors = []
        self.mode = 0   # 0: 대기 모드, 1: 일반 연산, 2: 팩토리얼

    # 계산기 동작 함수
    def run_calculator(self):
        first_operand = self.__check_not_integer(input())
        self.__egg_messages(first_operand)
        operator = input()
        self.__check_operator_valid(operator)   # 연산자 유효성 검사 및 모드 변화

        if (self.mode == 1):    # 일반 연산
            result = self.__calculate_normal(first_operand, operator)
        elif (self.mode == 2):  # 팩토리얼 연산
            result = self.__calculate_factorial(first_operand)
        else:   # 대기 모드
            result = first_operand
            while operator != "=":
                operator = input()

        self.__error_print()
        print(result)

    # 일반 연산 계산기
    def __calculate_normal(self, first_operand, operator):
        while operator != "=":
            next_operand = self.__check_not_integer(input())
            self.__egg_messages(next_operand)
            if operator == "+":
                first_operand += next_operand
            elif operator == "-":
                first_operand -= next_operand
            elif operator == "*":
                first_operand *= next_operand
            next_operator = input()
            self.__check_operator_valid(next_operator)
            self.__check_operator_same(operator, next_operator)
            operator = next_operator
        return first_operand
    
    # 팩토리얼 계산기
    def __calculate_factorial(self, number):
        result = self.__factorial(number)
        while 1:
            next_operator = input()
            if next_operator != "=":
                self.__errors.append(5)
            else:
                return result
    
    def __factorial(self, number):
        if self.__check_factorial_valid(number):
            if number == 0 or number == 1:
                return 1
            else:
                return number * self.__factorial(number - 1)
        return 0

    # 연산자 유효성 및 모드 체크
    def __check_operator_valid(self, operator):
        if operator in ["-", "+", "*"]:
            self.mode = 1
        elif operator == "!":
            self.mode = 2
        elif operator == "=":
            self.mode = 0
        else:
            try:
                if int(operator):
                    self.__errors.append(5) # errno5: input 에러
            except (ValueError):
                self.__errors.append(2) # errno2: 잘못된 연산자 에러
    
    # 연산자 연속성 체크
    def __check_operator_same(self, operator, next_operator):
        if operator != next_operator:
            if next_operator != '=':
                self.__errors.append(3) # errno3: 다른 연산 에러
    
    # 정수가 아닌 피연산자 입력 체크
    def __check_not_integer(self, input_operand):
        try:
            operand = int(input_operand)
        except (ValueError):
            self.__errors.append(1) # errno1: 정수가 아닌 피연산자 에러
            operand = 0.404 # 유효하지 않은 연산자 값(이스터에그를 발동시키지 않는 값으로 설정)
        return operand
    
    # 팩토리얼 피연산자 확인
    def __check_factorial_valid(self, number):
        if number < 0:
            self.__errors.append(4) # errno4: out of range 에러
            return 0
        return 1

    # error 메시지 출력 함수
    def __error_print(self):
        if not self.__errors:
            return
        for error in self.__errors: # 저장된 모든 에러 출력
            if error == '':
                return
            elif error == 1:
                print("[ERROR] Not Integer!")
            elif error == 2:
                print("[ERROR] Operator Invalid!")
            elif error == 3:
                print("[ERROR] Different Operator!")
            elif error == 4:
                print("[ERROR] Out Of Range!")
            elif error == 5:
                print("[SYSTEM] Input Error!")
        exit()
        
    # 이스터에그 함수, 특정한 숫자일 때 특별한 메시지 출력
    def __egg_messages(self, operand):
        if operand == 7:
            print("[EVENT] 행운")
        elif operand == 1221:
            print("[EVENT] 종강종강 돌을 던지자")
        elif operand == 18:
            print("[EVENT] 바른말고운말")
        elif operand == 0:
            print("[EVENT] 0은 여기서 False란다")
        elif operand == 1:
            print("[EVENT] 1은 여기서 True란다")
        elif operand == 2:
            print("[EVENT] Binary..?")
        elif operand == 534:
            print("[EVENT] 컴공생들의 무덤")
        elif operand == 1015:
            print("[EVENT] 전북대 개교기념일입니다.")

a = calculator()
a.run_calculator()
