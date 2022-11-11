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
# with open("filename", "r") as file
# print(file.readline()) -> with open은 자동으로 close 해줌, readline은 첫줄만 읽어줌


# Chapter 49 클래스 이해하기 (class) -> 거푸집이라고 이해
class MyClass:
    var = '안녕하세요'
    def sayHello(self):
        print(self.var) # MyClass 선언부 내에서 클래스 멤버를 지시할 때는 self.클래스멤버

obj = MyClass() # 인스턴스 객체: 클래스를 실제 사용 가능한 형태로 만듦
print(obj.var) # 안녕하세요 출력
obj.sayHello() # MyClass의 sayHello 호출, 메소드를 호출할 경우에는 self 생략
# 내용은 이해가 가는데 class가 뭐하는것인지 사실 잘 모르겠음


# Chapter 50 클래스 멤버와 인스턴스 멤버 이해하기
# 클래스 멤버: 클래스 메소드 바깥에서 선언, 인스턴스 멤버: 메소드 안에서 self와 함께 선언되는 변수
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

# 11/11 내용 추가

# class 생성자 -> 클래스 실행

class Slime: # -> slime 생성
    def __init__(self): # -> constructor, class로 변수를 호출(찍어낼때)할때 무조건 실행됨
        self.name = "slime"
        self.hp = 100
        self.attack = 5
        self.defense = 3
    def attacked(self, damage):
        self.hp -= (damage - self.defense)
    def __del__(self):
        print("Dobby is free~!!")

# self: class 자체를 가리킴, self.var는 무조건 class가 가지는 변수
# class 변수에 접근할때는 self. 으로 접근해야함
# 밖에서 호출할때는 self 생략 가능

slime1 = Slime() # -> 슬라임을 찍어낸것임
print("before attacked", slime1.hp)
slime1.attacked(50)
print("after attacked", slime1.hp)


# class destructor 메모리에서 사라질 때
del slime1 # -> 이거 없어도 코드 한번 다 돌면 메모리에서 지워짐
# 파이썬에서 많이 쓰지는 않음~


# Class 상속
class Monster: # -> base class
    def __init__(self):
        self.name = None
        self.hp = None
        self.attack = None
        self.defense = None
    def attacked(self, damage):
        self.hp -= (damage - self.defense)

class Slime(Monster): # -> 자식 class
    def __init__(self, hp=100):
        super().__init__() # super는 부모 class를 끌고옴, Monster에 있는 생성자 실행해주세요~

        self.name = 'slime'
        self.hp = hp
        self.attack = 5
        self.defense = 3
# slime은 Monster의 변수와 함수에 접근 가능

class Stump(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'stump'
        self.hp = 50
        self.attack = 2
        self.defense = 0

slime1 = Slime()
stump1 = Stump()

print(slime1.hp, stump1.hp)

slime1.attacked(20)
stump1.attacked(20)

print(slime1.hp, stump1.hp)

king_slime = Slime(hp=1000)
print(king_slime.hp)


# Chapter 55 예외처리 이해하기(try~except)
# error가 있을 수도 있는 상황에서 사용
# error가 있으면 except 처리, 프로그램 중지되지 않고 넘어가서 계속 실행

a = 4
b = 2

try:
    print(a/b)
except:
    print("there is error!") # error가 있으면 출력
else:
    print("No error!") # try가 정상적으로 실행되면 출력, for~else와 똑같음

print("talk to me, goose!")


# Chapter finally
# error가 있든 없든 무조건 실행


# Chapter 무슨 에러
c = 1
d = 0

try:
    print(c/d)
except Exception as event:
    print(event) # 어떤 error인지 알 수 있음


# 특정 error에만 관심이 있을 때

try:
    print(c/d)
except ZeroDivisionError: # 0으로 나누는 에러가 있을때만 실행
    print("hello")


# import time
# count = 1
#
# try:
#     while True:
#         print(count)
#         count += 1
#         time.sleep(0.5)
# except KeyboardInterrupt: # ctrl+c
#     print("Interrupt by idiot")

print("hello")