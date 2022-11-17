# Chapter 60 사용자 입력받기

# k = input('<값>을 입력하세요.')
# print('당신이 입력한 값은 <' + k + '>입니다.')


# Chapter 61 자료형 확인하기(type)
numdata = 57
strdata = '파이썬'
listdata = [1, 2, 3]
dictdata = {'a':1, 'b':2}

def func():
    print('안녕하세요')

print(type(numdata)) # int
print(type(strdata)) # str
print(type(listdata)) # list
print(type(dictdata)) # dict
print(type(func)) # function


# Chapter 62 나눗셈에서 나머지만 구하기(%)
a = 11113
b = 23
ret = a%b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.' %(a, b, ret))


# Chapter 63 몫과 나머지 구하기(divmod)
ret1, ret2 = divmod(a, b) # ret1: 몫, ret2: 나머지
print('<%d / %d>는 몫이 <%d>, 나머지가 <%d>입니다.' %(a, b, ret1, ret2))


# Chapter 64 10진수를 16진수로 변환하기(hex)
h1 = hex(97) # 0x61 문자열
h2 = hex(98) # 0x62 문자열
ret1 = h1 + h2
print(ret1) # 0x610x62 문자열로 출력

a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b # 십진수 195
print(hex(ret2)) # oxc3

n = 159
# %X와 %x는 16진수를 나타내는 포맷 문자열
print('%X' %n) # 대문자 9F
print('%x' %n) # 소문자 9f
# %02X, %02x를 사용하면 한 자리수 16진수 앞에 0을 붙여 표현
m = 11
print('%02X' %m) # 0B
print('%02x' %m) # 0b


# Chapter 65 10진수를 2진수로 변환하기(bin)
b1 = bin(97) # 0b11000001
b2 = bin(98) # 0b11000010
ret1 = b1 + b2
print(ret1)

a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b
print(bin(ret2))


# Chapter 66 2진수, 16진수를 10진수로 변환하기(int)
bnum = 0b11110000; bstr = '0b11110000'
onum = 0o360; ostr = '0o360'
hnum = 0xf0; hstr = '0xf0'
b1 = int(bnum); b2 = int(bstr, 2) #문자열은 2진수, 10진수, 16진수인지 표시
o1 = int(onum); o2 = int(ostr, 8)
h1 = int(hnum); h2 = int(hstr, 16)
print(b1); print(b2)
print(o1); print(o2)
print(h1); print(h2)


# Chapter 67 절댓값 구하기(abs)
abs1 = abs(-3) # 3
abs2 = abs(-5.72) # 5.72
abs3 = abs(3+4j) # sqrt(3^2 + 4^2) 출력
print(abs1); print(abs2); print(abs3)


# Chapter 68 반올림수 구하기(round)
ret1 = round(1118)
ret2 = round(16.554)
ret3 = round(1118, -1) # 1자리에서 반올림
ret4 = round(16.554, 2) # 소수점 셋째자리에서 반올림
print(ret1); print(ret2); print(ret3); print(ret4)


# Chapter 69 실수형 자료를 정수형 자료로 변환하기(int)
idata1 = int(-5.4)
idata2 = int(1.78e1)
idata3 = int(171.56)
print(idata1); print(idata2); print(idata3)
# 소수부분 버리고 정수 부분만 가져옴


# Chapter 70 정수형 자료를 실수형 자료로 변환하기(float)
fdata = float(10) # 10.0
print(fdata)


# 정수 리스트에서 소수만 걸러내기(filter)
def getPrime(x):
    if x%2 == 0: # 짝수면 반환
        return

    for i in range(3, int(x/2), 2): # 3부터 간격이 2인 홀수로 나눴을 때 나눠떨어지면 소수가 아님
        if x%i == 0:
            break
    else:
        return x

listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))

# 주어진 정수 n 이하의 모든 소수를 구하는 함수
def getPrime2(n):
    ret = [2]
    if n == 1:
        print('2 이상의 정수를 입력하세요.')
        ret = ['none']

    if n == 2:
        return ret

    for i in range (3, n+1, 2):
        for k in range (3, int(i/2), 2):
            a = i%k
            if a == 0:
                break
        else:
            ret.append(i)
    return ret

# n = 1이면 2이상의 정수를 입력하도록 수정하였음!! 아래가 원래 코드!!
# def getPrime2(n):
#     ret = [2]
#     if n <= 2:
#         return ret
#
#     for i in range (3, n+1, 2):
#         for k in range (3, int(i/2), 2):
#             a = i%k
#             if a == 0:
#                 break
#         else:
#             ret.append(i)
#     return ret

ret = getPrime2(1)
print(ret)


# Chapter 72 최대값, 최솟값 구하기(max, min)
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata) # 9.96
minval = min(listdata) # 0.93
print(maxval); print(minval)

txt = 'Alotofthingsoccureachday'
maxval = max(txt) # y 문자열 최대는 알파벳 순서로 가장 뒤의 문자
minval = min(txt) # A 문자열 최소는 알파벳 순서로 가장 앞의 문자
print(maxval); print(minval)

maxval = max(2+3, 2*3, 2**3, 3**2) # 9
minval = min('abz', 'al2') # al2 이건 왜 최소가 얘입니까?? 코드값 알아야합니까??
print(maxval); print(minval)


# Chapter 73 1바이트에서 하위 4비트 추출하기
a = 107 # 16진수로 0x6b
b = a & 0x0f # 00001111과 연산해서 하위 4비트만 추출
print(b) # 0xb
# 그냥 알아서 비트연산을 해준다~ 라고 이해하면 되는지???


# Chapter 74 1바이트에서 상위 4비트 추출하기
b = (a>>4) & 0x0f # 4만큼 오른쪽으로 보내면 상위 4비트가 하위 4비트가 됨, 마찬가지로 00001111과 연산하여 추출
print(b)


# Chapter 75 문자열에서 특정 위치의 문자 얻기
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[5]) # e
print(txt2[-2]) # 라


# Chapter 76 문자열에서 지정한 구간의 문자열 얻기
print(txt1[3:7]) # ale 7번째 미만!!!까지 출력
print(txt1[:6]) # A tale
print(txt2[-4:]) # 가리라.

txt = 'python'
for i in range(len(txt)): # 길이 6
    print(txt[:i+1])

# [:2] p
# [:3] py
# [:4] pyt
# [:5] pyth
# [:6] pytho
# [:7] python


# Chapter 77 문자열에서 홀수 번째 문자만 추출하기
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2] # 처음부터 끝까지 스텝은 2(처음 문자부터 추출)
print(ret)
# 짝수 번째 문자만 추출
ret = txt[1::2]
print(ret)