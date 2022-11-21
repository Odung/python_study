# Chapter 78 문자열을 거꾸로 만들기
txt = 'abcdefghijk'
ret = txt[::-1] # 처음부터 끝까지 스텝 -1로 슬라이싱
print(ret)

ret1 = txt[::-2]
ret2 = txt[-2::-2]
print(ret1); # 거꾸로 된 순서에서 홀수번째
print(ret2); # 거꾸로 된 순서에서 짝수번째


# Chapter 79 두 개의 문자열 합치기(+)
# filename = input('저장할 파일이름을 입력하세요:')
# filename = filename + '.jpg'
# display_msg = '당신이 저장한 파일은 <' + filename + '>입니다.'
# print(display_msg)


# Chapter 80 문자열을 반복해서 새로운 문자열로 만들기(*)
msg1 = '여러분'
msg2 = '파이팅!'
display_msg = msg1 + ',' + msg2*3 + '~!'
print(display_msg)


# Chapter 81 문자열에서 특정 문자가 있는지 확인하기(in)
# msg = input('임의의 문장을 입력하세요.')
# if 'a' in msg:
#     print('당신이 입력한 문장에는 a가 있습니다.')
#
# else:
#     print('당신이 입력한 문장에는 a가 없습니다.')


# Chapter 82 문자열에서 특정 문자열이 있는지 확인하기(in)
# msg = input('임의의 문장을 입력하세요.')
# if 'is' in msg:
#     print('당신이 입력한 문장에는 is가 있습니다.')
#
# else:
#     print('당신이 입력한 문장에는 is가 없습니다.')


# Chapter 83 문자열 길이 구하기(len)
# msg = input('임의의 문장을 입력하세요')
# msglen = len(msg)
# print('당신이 입력한 문장의 길이는 <%d>입니다.' %msglen)
# 주의: 문자열 길이가 같아도 바이트 객체 크기는 다를 수 있음 (한글 / 영어)


# Chapter 84 문자열이 알파벳인지 검사하기 (isalpha)
# 언어로만 입력되어있으면 True, 숫자나 공백 등이 포함되어있으면 False
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'

ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1); print(ret2); print(ret3); print(ret4)


# Chapter 85 문자열이 숫자인지 검사하기 (isdigit)
txt1 = '010-1234-5678' # 하이픈이 있으므로 False
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()

print(ret1); print(ret2); print(ret3)


# Chapter 86 문자열이 알파벳 또는 숫자인지 검사하기(isalnum)
# 문자와 숫자만으로 이루어져있을때 True
txt1 = '안녕하세요?'
txt2 = '1. Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()

print(ret1); print(ret2); print(ret3)


# Chapter 87 문자열에서 대소문자 변환하기(upper, lower)
txt = ' A lot of Things occur each day'
ret1 = txt.upper() # 전부 대문자로 변환
ret2 = txt.lower() # 전부 소문자로 변환
print(ret1); print(ret2)