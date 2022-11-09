# Chapter 32 멤버체크 이해하기 (in)
# 자료에 어떤 값이 있는지 확인
listdata = [1, 2, 3, 4]
ret1 = 5 in listdata # 5 없으니까 False
ret2 = 4 in listdata # 4 있으니까 True
print(ret1); print(ret2)

strdata = 'abcde'
ret3 = 'c' in strdata # True
ret4 = '1' in strdata # False
print(ret3); print(ret4)


# Chapter 33 문자열 이해하기
strdata1 = '나는 파이썬 프로그래머다' # 거짓말 흑흑
strdata2 = "You are an idot."
strdata3 = """I love
python. You love
python too!
""" # """이용하면 줄바꿔도 문자열로 정의 가능 그런데 출력도 줄바꿔서 되네...
print(strdata1); print(strdata2); print(strdata3)
strdata4 = "My friend's name is Goose" # ' 있으면 ""로 묶음
strdata5 = '문자열 "abs"의 길이는 3입니다.' # " 있으면 ''로 묶음
print(strdata4); print(strdata5)


# Chapter 34 문자열 포맷팅 이해하기
txt1 = '자바'; txt2 = '파이썬'
num1 = 5; num2 = 10
print('나는 %s보다 %s에 익숙합니다.' %(txt1, txt2))
print('%s는 %s보다 %d배 더 쉽습니다.' %(txt2, txt1, num1))
print('%d + %d = %d' %(num1, num2, num1 + num2))
print('작년 나의 키는 전년에 비해 %d%% 정도 증가했다' %num2) # 성장기라서 그렇군!

from time import sleep
for i in range(100):
    msg = '\r진행률 %d%%' %(i+1)
    print(' '*len(msg), end = '') # 얘가 뭐하는앤지 이해가 잘 안감 없어도 똑같이 돌아가는데요? 뭔지 이해만 하면됨 ㅇㅋ
    print(msg, end = '')
    sleep(0.1) # 0.1초 단위로 진행률 올라가도록?
# from 모듈 import 이름: 모듈 내에서 필요한 것을 가져옴
# 여기서는 파이썬의 time 모듈 이용, sleep 함수는 입력된 초만큼 스레드 정지
# 캐리지 리턴 문자 '\r': 맨 앞으로 이동


# Chapter 35 이스케이프 문자 이해하기
print('나는 파이썬을 사랑합니다. \n파이썬은 자바보다 훨씬 쉽습니다.')
print('Name: Pete Mitchell \tRank: Captain \tCallsign: Maverick') # 톡투미구스!!!
print('이 문장은 화면폭에 비해 너무 길어 보기가 힘듭니다. \
그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했습니다.')
print('작은따옴표(\')와 큰따옴표(")는 문자열을 정의할 때 사용합니다')


# Chapter 36 리스트 이해하기([])
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c']]
list1[0] = 6 # 1이 6으로 바뀜
print(list1)

def myfunc():
    print('안녕하세요')
list4 = [1, 2, myfunc]
list4[2]() # 안녕하세요 출력


# Chapter 37 튜플 이해하기(())
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])
# tuple1[0] = 6 # 값 수정 불가능

tuple4 = (1, 2, myfunc)
tuple4[2]() # 안녕하세요 출력


# Chapter 38 사전 이해하기 ({})
dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a']) # Value인 1 출력
dict1['d'] = 4 # ket와 Value를 추가
print(dict1) # Ket와 Value 함께 출력
dict1['b'] = 7 # 2를 7로 바꿈
print(dict1)
print(len(dict1)) # Key-Value 쌍의 개수(쌍이 하나의 요소임)


# Chapter 39 함수 이해하기(def)
# return이 꼭 필요한 경우는 언제일까???
def add_number(n1, n2):
    ret  = n1 + n2
    return ret

def add_number(n1, n2):
    print(n1 + n2) # 흠 얘도 꼭 return으로 지정할 필요는 없군

def add_txt(t1, t2):
    print(t1 + t2) # return 값이 없는 경우 return만 쓰거나 생략

ans = add_number(10, 15)
print(ans)
text1 = 'Talk to me '
text2 = 'Goose'
add_txt(text1, text2)
add_number(3, 5)


# Chapter 40 함수 인자 이해하기
def add_txt(t1, t2='파이썬'): # t2에 값 대입하지 않으면 기본값은 파이썬
    print(t1 + ':' + t2)

add_txt('베스트') # 베스트:파이썬
add_txt(t2 = '대한민국', t1 = '1등') # 1등:대한민국

def func1(*args): # *: 인자 개수가 불분명할 때 가변 인자, 튜플로 처리
    print(args)

def func2(width, height, **kwargs): # 키워드 인자가 불분명한 경우 **, 사전으로 처리
    print(kwargs)

func1() # 빈 튜플()
func1(3, 5, 1, 5) # (3, 5, 1, 5) 출력
func2(10, 20) # 빈 사전 {}, **kwargs에 해당하는 값이 없으므로 빈 사전
func2(10, 20, depth=50, color='blue') # {depth:50, color='blue'} 출력


# Chapter 41 지역변수와 전역변수 이해하기(global)
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param # global을 붙이면 전역변수 값을 변경
    param = 50

func1() # 지역변수
print(strdata) # 전역변수
print(param) # 10
func2(param)
print(param) # 10
func3()
print(param) # 50
# 함수의 인자로 선언된 변수는 함수 내에서만 유효한 지역변수임


# Chapter 42 함수 리턴값 이해하기(return)
def reverse(x, y, z):
    return(z, y, x)

ret = reverse(1, 2, 3)
print(ret) # 튜플로 리턴값 만듦

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3) # 각각 c, b, a


# Chapter 43 파이썬 모듈 이해하기

print('stop program for 5 seconds.')
# time.sleep(5) 5초간 정지
print('5 seconds passed.')

import mylib
ret1 = mylib.add_txt('대한민국', '1등')
ret2 = mylib.reverse(1, 2, 3)
print(ret1)
print(ret2)
# 우왕 신기해


# Chapter 44 파이썬 패키지 이해하기
# Chapter 45 파이썬 모듈 임포트 이해하기(import)
