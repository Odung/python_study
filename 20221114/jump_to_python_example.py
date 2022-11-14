# 4장 연습문제

# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수 (is_odd)를 작성해보자.

def is_odd(a):
    if a%2 == 0:
        print("%s는 짝수입니다." %a)
    else:
        print("%s는 홀수입니다." %a)

is_odd(346234)


# Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(3249, 234, 435, 14, 5))


# Q3 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해보자.
# input은 입력되는 모든 것을 문자열로 취급함

''' input1 = input("첫 번째 숫자를 입력하세요.")
input2 = input("두 번째 숫자를 입력하세요.")

total = int(input1) + int(input2) # int를 이용해서 문자열을 십진수 형태로 바꿔줌
print("두 수의 합은 %s 입니다" %total)
print(total) '''


# Q4 다음 중 출력 결과가 다른 것 한 개를 골라보자.

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python") # 콤마가 잇으면 공백이 삽입되어 더해짐
print("".join(["you", "need", "python"]))


# Q5 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

f1 = open("test.txt", 'w') # w는 쓰기모드
f1.write("Life is too short")
f1.close() # 파일을 닫지 않고 다시 열려고 하면 오류가 생겨서 close를 추가해 주어야 함

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


# Q6. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# 파일 추가 모드 'a'
with open("test.txt", 'a') as f3:
    f3.write("\n you need java") # with문을 사용하면 자동으로 close 됨


# Q7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java
# ※ replace 함수를 사용해 보자.

f4 = open("test.txt", 'r')
script = f4.read()
f4.close()

script = script.replace('java', 'python')

f = open("test.txt", 'w')
f.write(script)
f.close()


# 5장 연습문제
# Q1 다음은 Caculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value= 0

    def add(self, val):
        self.value += val

# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value) # 10에서 7을 뺀 3을 출력

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value) # 7 출력됨


# Q2 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.
#
# cal = MaxLimitCalculator()
# cal.add(50) # 50 더하기
# cal.add(60) # 60 더하기
# print(cal.value) # 100 출력
# 단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value + val <= 100:
            self.value += val
        else:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기
print(cal.value)


# 이건 답지인데 더 간지나는것같넹...흑흑
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100