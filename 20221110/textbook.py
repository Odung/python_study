# Chapter 46 파이썬 모듈 임포트 이해하기 (from~import)
# from 모듈이름 import 함수이름
# from 패키지이름 import 모듈이름


# Chapter 47 파이썬 모듈 임포트 이해하기 (import~as)
# 모듈 이름이 길거나 계층구조가 복잡한 경우 모듈에 별명을 붙일 수 있음
# import 이름이 긴 모듈명 as 별명
'''import mypackage as mp -> mypackage를 mp로 축약
   import mypackage.mylib as ml -> mypachage.mylib을 ml로 축약'''


# Chapter 48 파일 열고 닫기 (open, close)
# open(파일이름, 모드), 경로 정보가 없으면 프로그램 구동 디렉터리에서 파일을 찾음
# filename.close(), 오픈한 파일 닫기


# Chapter 49 클래스 이해하기 (class)
class MyClass:
    var = '안녕하세요'
    def sayHello(self):
        print(self.var) # MyClass 선언부 내에서 클래스 멤버를 지시할 때는 self.클래스멤버

obj = MyClass() # 인스턴스 객체: 클래스를 실제 사용 가능한 형태로 만듦
print(obj.var) # 안녕하세요 출력
obj.sayHello() # MyClass의 sayHello 호출, 메소드를 호출할 경우에는 self 생략
# 내용은 이해가 가는데 class가 뭐하는것인지 사실 잘 모르겠음


# Chapter 50 클래스 멤버와 인스턴스 멤버 이해하기
# 클래스 멤버: 쿨래스 메소드 바깥에서 선언, 인스턴스 멤버: 메소드 안에서 self와 함께 선언되는 변수
class MyClass():
    var = '안녕하세요!!'
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var) # 안녕하세요!!
obj.sayHello() # 안녕 + 안녕하세요!!
print(obj.param2) # 윗줄 이후에 참조해야 오류가 안생김 ???


# Chapter 51 클래스 메소드 이해하기
class MyClass:
    def sayHello(selfself):
        print('안녕하세요')

    def sayBye(selfself, name):
        print('%s! 다음에 보자!' %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('오리박')


# Chapter 52 클래스 생성자 이해하기
class MyClass:
    def __init__(self):
        self.var = '안녕하세요!'
        print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass()
print(obj.var)


# Chapter 53 Class 소멸자 이해하기
class MyClass:
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj = MyClass()
del obj


# Chapter 54 Class 상속 이해하기
class Add:
    def add(selfself, n1, n2):
        return n1 + n2

class Calculator(Add):
    def sub(selfself, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2)) # 3
print(obj.sub(1, 2)) # -1

# 다중상속 부럽당
class Multiply:
    def multiply(self, n1, n2):
        return n1*n2

class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2)) # 3
print(obj.sub(1, 2))
print(obj.multiply(3, 2)) # 6

# 클래스 내용이 어렵습니당!!