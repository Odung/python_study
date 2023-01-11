# Chapter 88 문자열에서 좌우 공백 제거하기

txt = ' 양쪽에 공백이 있는 문자열입니다. '
ret1 = txt.lstrip() # 왼쪽 공백 제거
ret2 = txt.rstrip() # 오른쪽 공백 제거
ret3 = txt.strip()

print('<'+txt+'>')
print('<'+ret1+'>')
print('<'+ret2+'>')
print('<'+ret3+'>')


# Chapter 89 문자열을 수치형 자료로 변환하기
# numstr = input('숫자를 입력하세요: ')
# try:
#     num = int(numstr)
#     print('당신이 입력한 숫자는 정수 <%d>입니다.' %num)
# except:
#     try:
#         num = float(numstr)
#         print('당신이 입력한 숫자는 실수 <%f>입니다.' %num)
#     except:
#         print('+++숫자를 입력하세요~+++')


# Chapter 90 수치형 자료를 문자열로 변환하기
num1 = 1234
num2 = 3.14

numstr1 = str(num1)
numstr2 = str(num2)
print('num1을 문자열로 변환한 값은 "%s"입니다.'%numstr1)
print('num2을 문자열로 변환한 값은 "%s"입니다.'%numstr2)

print('num1값은 %f입니다.' %num1) # 그냥 이렇게 출력해도 될것같은데 흠
print('num2값은 %f입니다.' %num2)


# Chapter 91 문자열에 있는 문자(열) 개수 구하기
txt = 'A lot of things occur each day, every day.'
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ') # 공백 개수

print(word_count1)
print(word_count2)
print(word_count3)


# Chapter 92 문자열에서 특정 문자(열) 위치 찾기
offset1 = txt.find('e') # 공백까지 포함
offset2 = txt.find('day')
offset3 = txt.find('day', 30) # 30번 인덱스 이후부터 찾기

print(offset1); print(offset2); print(offset3)


# Chapter 93 문자열을 특정 문자(열)로 분리하기(split)
url = 'http://www.naver.com/news/todasy=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/') # /기준으로 분리
print(ret1)

ret2 = log.split() # 디폴트는 공백 분리
print(ret2)
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s'%(d1, d2))

# Chapter 94 문자열을 특정 문자(열)로 결합하기(join)
loglist = ['2016/08/26 10:12:11', 'OK', '이 또한 지나가리라']
bond = ';' # James Bond~
log = bond.join(loglist) # 세미콜론으로 연결
print(log)


# Chapter 95 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기
txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print(ret1); print(ret2)

txt = '매일 많은 일들이 일어납니다.'
ret3 = txt.replace('매일', '항상')
ret4 = ret3.replace('일', '사건')
print(ret3); print(ret4)


# Chapter 96 문자열을 바이트 객체로 바꾸기
u_txt = 'I love python'
b_txt = u_txt.encode() # 디폴트는 UTF-8
print(u_txt); print(b_txt) # 바이트 객체는 앞에 b 붙어서 출력

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)
print(ret2) # 바이트로 바꿨으므로 73임 따라서 False 출력
print(b_txt[0])


# Chapter 97 바이트 객체를 문자열로 바꾸기
b_txt = b'A lot of things occur each day' # 바이트 객체 문자열
u_txt = b_txt.decode()
print(u_txt) # b가 빠진 문자열로 표시


# Chapter 98 문자열을 정렬하기
# strdata = input('정렬할 문자열을 입력하세요: ')
# ret1 = sorted(strdata) # 오름차순
# ret2 = sorted(strdata, reverse=True) # 내림차순
# print(ret1)
# print(ret2)
#
# ret1 = ''.join(ret1)
# ret2 = ''.join(ret2)
# print('오름차순으로 정렬된 문자열은 <' +ret1+ '>입니다.')
# print('내림차순으로 정렬된 문자열은 <' +ret2+ '>입니다.')


# Chapter 99 순차적인 정수 리스트 만들기
range1 = range(10) # 10 전까지
range2 = range(10, 20) # 20 전까지
print(list(range1))
print(list(range2))

ret = 0
for i in range(10):
    ret += (i+1) # 1부터 10까지 모두 더하기
print(ret)


# Chapter 100 리스트에서 특정 위치의 요소 얻기
listdata = [1, 2, 'a', 'b', 'c', [4, 5, 6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
print(val1); print(val2); print(val3)