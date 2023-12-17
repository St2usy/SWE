import unittest
class calculator:
    def __init__(self):
        self.__errno = 0
    def  get_errno(self):
        return self.__errno
    # 계산기 작동 함수
    def run_calculator(self):
        first_operand = self.__check_not_integer(input())  # 첫번째 피연산자 입력 및 유효성 확인
        self.__egg_messages(first_operand)  # 이스터에그 함수 수행
        operator = input()  # 연산자 입력

        # 연산자가 '='이 나오기 전까지 동작
        while operator != '=':
            next_operand = self.__check_not_integer(input()) # 다음 피연산자 입력 및 유효성 확인
            self.__egg_messages(next_operand) # 이스터에그 함수 수행
            self.__check_operator_valid(operator) # 연산자 유효성 검사
            next_operator = input()  # 다음 연산자 입력
            self.__check_operator_same(operator, next_operator) # 동일 연산 검사
            first_operand = self.__calculate(first_operand, next_operand, operator) # 연산 수행
            operator = next_operator

        self.__error_print()
        print(first_operand)  # 계산 결과 출력

    # 연산 수행 함수 -> 테스팅 진행
    def calculate(self, first_operand, next_operand, operator):
        result = 0
        if self.__errno != 0:  # 에러가 발생했을 시 수행 없이 바로 리턴
            return result
        if operator == "+":
            result = first_operand + next_operand
        elif operator == "-":
            result = first_operand - next_operand
        elif operator == "*":
            result = first_operand * next_operand
        return result

    # error 체크 함수
    # 유효하지 않은 연산자 체크 -> 테스팅 진행
    def check_operator_valid(self, operator):
        if(operator == '+' or operator == '-' or operator == '*'):
            self.__errno = 0
        else:
            self.__errno = 2
    # 다른 연산자 입력 체크
    def __check_operator_same(self, first_operator, next_operator):
        if first_operator != next_operator :
                if next_operator != '=':  # 다른 연산이면 등호인지 확인
                    self.__errno = 3
    # 정수가 아닌 피연산자 입력 체크 
    def check_not_integer(self, input_operand):
        try:
            self.__errno = 0
            operand = int(input_operand)
        except (ValueError):
            self.__errno = 1
            operand = 0.404 # 유효하지 않은 연산자 값(이스터에그를 발동시키지 않는 값으로 설정)
        return operand

    # error 메시지 출력 함수
    def __error_print(self):
        if self.__errno == 0:
            return
        elif self.__errno == 1:
            print("[SYSYEM] NOT INTEGER ERROR!")
        elif self.__errno == 2:
            print("[SYSYEM] OPERATOR INVALID ERROR!")
        elif self.__errno == 3:
            print("[SYSTEM] DIFFERENT OPERATOR ERROR!")
        exit()

    # 이스터에그 함수, 특정한 숫자일 때 특별한 메시지 출력 -> 테스팅 진행
    def egg_messages(self, operand):
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
            
class TestCalculate(unittest.TestCase) :
    def test_positive_numbers(self):
        calc = calculator()
        self.assertEqual(calc.calculate(5,3,'+'), 8)
        self.assertEqual(calc.calculate(5,3,'-'), 2)
        self.assertEqual(calc.calculate(5,3,'*'), 15)
    def test_negative_numbers(self):
        calc = calculator()
        self.assertEqual(calc.calculate(-5,-3,'+'), -8)
        self.assertEqual(calc.calculate(-5,-3,'-'), -2)
        self.assertEqual(calc.calculate(-5,-3,'*'), 15)
    def test_string(self):
        calc = calculator()
        self.assertEqual(calc.calculate('1','2','+'), '12')

class TestCheckOperatorValid(unittest.TestCase) :
    def test_valid(self):
        calc = calculator()
        result = calc.check_operator_valid('+')
        self.assertEqual(calc.get_errno(), 0)
        result = calc.check_operator_valid('-')
        self.assertEqual(calc.get_errno(), 0)
        result = calc.check_operator_valid('*')
        self.assertEqual(calc.get_errno(), 0)
    def test_notvalid(self):
        calc = calculator()
        result = calc.check_operator_valid('/')
        self.assertEqual(calc.get_errno(), 2)
        result = calc.check_operator_valid(1)
        self.assertEqual(calc.get_errno(), 2)

class TestCheckNotInteger(unittest.TestCase):
    def test_integer(self):
        calc = calculator()
        self.assertEqual(calc.check_not_integer('123'), 123)
        self.assertEqual(calc.check_not_integer('0'), 0)
        self.assertEqual(calc.check_not_integer('-123'), -123)
        self.assertEqual(calc.check_not_integer('123456789123123123'), 123456789123123123)
    def test_notinteger(self):
        calc = calculator()
        result = calc.check_not_integer('4.1')
        self.assertEqual(calc.get_errno(),1)
        result = calc.check_not_integer('+')
        self.assertEqual(calc.get_errno(),1)
        result = calc.check_not_integer('')
        self.assertEqual(calc.get_errno(),1)

if __name__ == '__main__' :
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculate))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCheckOperatorValid))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCheckNotInteger))

    unittest.TextTestRunner().run(suite)
                         
