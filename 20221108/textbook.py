# Chapter 16 정수형 자료 이해하기

bin_data = 0b10 # 2진수
oct_data = 0o10 # 8진수
hex_data = 0x10 # 16진수
print(bin_data) # 2
print(oct_data) # 8
print(hex_data) # 16


# Chapter 17 실수형 자료 이해하기

f3 = 1.56e3 # e3 = 10^3
f4 = -0.7e-4 # e4 = 10^(-4)
print(f3)
print(f4) # -7e-05로 출력해줌


# Chapter 18 복소수형 자료 이해하기

c1 = 1+7j
print(c1.real); print(c1.imag) # real: 실수부, imag: 허수부
c2 = complex(2, 3) # 복소수 생성
print(c2)


# Chapter 19 대입 연산자 이해하기
# =는 대입, ==는 같다
a = 1; b = 2
ret = a + b
print('a와 b를 더한 값은', end=" ")
print(ret, end = "")
print('입니다.')


# Chapter 20 사칙 연산자 이해하기
a = 2; b = 4
ret5 = a**b # **는 거듭제곱
ret6 = a + a*b/a # 연산 우선순위: 거듭제곱 > 곱셉/나눗셈 > 덧셈/뺄셈


# Chapter 21 연산자 축약 이해하기
a = 0
a += 1 # a = a + 1
a -= 5 # a = a - 5
a *= 2 # a = a*2
a /= 4 # a = a/4


# Chapter 22 True와 False 이해하기
a = True
b = False
print(a == 1) # a가 1이면 True, 아니라면 False
print(b != 0) # b가 0이라면 False, 0이 아니라면 True
# True와 False로 나타내면 더 직관적이고 프로그램 코드의 가독성을 높일 수 있다는게 머선 말인고 ??
# while True: 무한 반복 실행 (여기서 True는 특별한 의미가 없는것인고 ??)


# Chapter 23 관계 연산자 이해하기
x = 1; y = 2
str1 = 'abc'; str2 = 'python'
print(x != y) # x와 y가 다르면 참
print(str1 == str2) # 연산자는 문자열에도 적용 가능(모든 자료형에 적용 가능)


## Chapter 24 논리 연산자 이해하기
bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2) # 둘 모두 참이면 참 False
print(bool1 and bool3) # True
print(bool2 or bool3) # 하나 이상이 참이면 참 True
print(bool2 or bool4) # False
print(not bool1) # False 출력
print(not bool2) # True 출력


# Chapter 25 비트 연산자 이해하기
# 보수 만들기는 어떻게 합니까?!

bit1 = 0x61 # 16진수 -> 2진수로는 0110 0001
bit2 = 0x62 # 2진수로 0110 0010
print(hex(bit1 & bit2)) # bit간 and 연산 (연산은 2진수에서 이뤄지는것인가 ?!)
print(hex(bit1 | bit2)) # bit간 or 연산
print(hex(bit1 ^ bit2)) # xor 연산, 비트값이 같으면 0, 다르면 1
print(hex(bit1 >> 1)) # 오른쪽으로 1만큼 시프트, 없어지는 값은 0으로 채움
print(hex(bit1 << 2)) # 왼쪽으로 2만큼 시프트


# Chapter 26 시퀀스 자료형 이해하기
# 순서를 가지고 나열되어 있으면 시퀀스 자료형: 문자열, 리스트, 튜플
# 음~ 그렇군요!


# Chapter 27 시퀀스 자료 인덱싱 이해하기
strdata = 'Time is money!!'
listdata = [1, 2, [1, 2, 3]]
print(strdata[5]) # 띄어쓰기도 요소에 포함임
print(strdata[-2])
print(listdata[0])
print(listdata[-1])
print(listdata[2][-1]) # 3 출력


# Chapter 28 시퀀스 자료 슬라이싱 이해하기
# 시작 인덱스 이상부터 끝 인덱스 미만까지, 단 :은 끝까지
print(strdata[1:5]) # ime
print(strdata[:7]) # Time is
print(strdata[9:]) # oney!!
print(strdata[:-3]) # Time is mone
print(strdata[-3:]) # y!!
print(strdata[:]) # Time is money!!
print(strdata[::2]) # 처음부터 끝까지, 스텝은 2 Tm smny!


# Chapter 29 시퀀스 자료 연결 이해하기(+)
strdata1 = 'I love'; strdata2 = 'Python'; strdata3 = 'you'
listdata1 = [1, 2, 3]; listdata2 = [4, 5, 6]
print(strdata1 + strdata2)
print(strdata1 + strdata3)
print(listdata1 + listdata2) # 리스트 형태로 출력


# Chapter 30 시퀀스 자료 반복 이해하기(*)
mitchell = 'Maverick!'
bradshaw = 'Goose'
dispdata = bradshaw + '가 말합니다. Talk to me' + ' ' + mitchell*3
# 음 뭔가 이상하지만 마음에 들어용
print(dispdata)

# Chapter 31 시퀀스 자료 크기 이해하기(len)
strdata1 = 'Talk to me goose!'
strdata2 = '나는 오리박을 사랑합니다.' # 우하하
listdata = ['a', 'b', 'c', strdata1, strdata2]
print(len(strdata1)) # 13 띄어쓰기까지 포함
print(len(strdata2)) # 14
print(len(listdata)) # 5
print(len(listdata[3])) # 13