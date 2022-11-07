# 2장 연습문제

'''Q1 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
국어: 80, 영어: 75, 수학: 55'''
test_score = [80, 75, 55] #저런 수학을 정말 못하네...
avg_score = sum(test_score)/len(test_score)
print(avg_score)


'''Q2 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자.'''
# 2로 나눴을 때 나누어 떨어지면 짝수, 나머지가 1이면 홀수
# 나누기:/, 몫://, 나머지:%
if 13%2 == 0:
    print("13은 짝수입니다.")
else:
    print("13은 홀수입니다.")


'''Q3 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월(YYYYMMDD)일 부분과 그 뒤의 숫자부분으로 나누어 출력해보자'''
pin = "881120-1068234"
birth = pin[0:6]
num = pin[7:14]
print(birth)
print(num)


'''Q4주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.'''
pin = "881120-1068234"
print(pin[-7])


'''Q5 다음과 같은 분자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자.'''
a = "a:b:c:d"
print(a.replace(":", "#"))


'''Q6 [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.'''
# 먼저 정렬하고 뒤집기
b = [1, 3, 5, 4, 2]
b.sort()
b.reverse()
print(b)


'''Q7 ['life', 'is', 'too', 'short']리스트를 Life is too short 문자열로 만들어 출력해 보자.'''
c = ['life', 'is', 'too', 'short']
c1 = " ".join(c) # list의 요소 사이에 공백 추가
# 복잡하고 쓸데없지만 이것도 가능: c2 = c[0] + " " + c[1] + " " + c[2] + " " + c[3]
print(c1)
# print(c2)


'''Q8 (1, 2, 3)튜플에 값 4를추가하여 (1, 2, 3, 4)를 만들어 출력해 보자.'''
d1 = (1, 2, 3)
d2 = (4,) # 튜플에 element가 1개만 있을 때는 뒤에 꼭 ,를 붙여주기
print(d1 + d2)


'''Q9 다음과 같은 딕셔너리 e1이 있다. e_d = dict()
다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.'''
e_d = dict()
e_d['name'] = 'python'
e_d[('a',)] = 'python'
# e_d[[1]] = 'python' # key에 list형태 넣을 수 없음, value에는 가능, 단 tuple은 key로 가능
e_d[250] = 'python'


'''Q10 딕셔너리 f에서 'B'에 해당되는 값을 추출해 보자.'''
f = {'A':90, 'B':80, 'C':70}
print(f['B'])

# pop 함수로는 어떻게?
result_f = f.pop('B') # f에서 'B':80 제거됨
print(result_f)


'''Q11 리스트에서 중복 숫자를 제거해 보자.'''
g = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
g_set = set(g) # 집합은 중복 허용하지 않음
g = list(g_set) # 다시 list로 바꾸기
print(g)


'''Q12 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
다음과 같이 h, i 변수를 선언한 후 h의 두 번재 요솟값을 변경하면 i 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.'''
h = i = [1, 2, 3]
h[1] = 4
print(i)
# 답: [1, 4, 3]이 출력된다. a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있기 때문이다. 흠




# 3장 연습문제
'''Q1 다음 코드의 결괏값은 무엇일까?'''

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
# shirt 출력


'''Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자'''
number = 0
number_list = []

while True:
    number += 3
    if number >= 1000:
        break
    number_list += [number] # 이러면 999까지 걸림 순서가 중요!!

print(sum(number_list)) # 오 내가짰지만 좀 잘 짠듯 풉킼

# solution 코드(이게 더 고급진것같다 흑흑)
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1
#
# print(result) # 166833 출력


'''Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.'''
star = "*"

while True:
    print(star)
    star += "*"
    if len(star) > 5:
        break


'''Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.'''

result = [i for i in range(1, 101)]
print(result)


'''Q5 A학급에 총 10명의학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. for문을 하용하여 A 학급의 평균 점수를 구해 보자.'''
A_score = [70, 60, 55, 75, 95, 90, 80, 85, 100] # 굳이 for문을 이용하여 문제를 어렵게 풀어야 합니까?
sum_A = 0
for x in range(len(A_score)):
    sum_A += A_score[x]
# 아래는 solution 
# for score in A:
#     total += score   # A학급의 점수를 모두 더한다.

avg_A = sum_A/len(A_score)
print(avg_A)


'''Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포를 사용하여 표현해 보자.'''

numbers = [1, 2, 3, 4, 5]
result_q6 = [n*2 for n in numbers if n%2 == 1]
print(result_q6)