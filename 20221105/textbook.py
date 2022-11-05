import keyword # keyword를 가져옴
print(keyword.kwlist)

import math # 음~
print(math.pi)

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

list_data[2]=100
print(list_data)

# tuple_data[2]=100
# print(tuple_data)

dict_data = {'name':'Maverick', 'age':61}
print(dict_data['age'])

print('#', end="+")
print('#')

listdata = ['a', 'b', 'c']
if 'a' in listdata:
    print('a가 있습니다')
    print(listdata)
else:
    print('a가 없습니다')

x = 3
y = 5
if x < y:
    print(1)
elif x == y:
    print(2)
elif x > y:
    print(3)

for data in listdata:
    print(data)

a = list(range(1, 101, 2)) # 간격 만들기
print(a)
# for number in a:
#     print(number)

string_data = "I'm happy"
for c in string_data:
    print(c)

for key in dict_data:
    print(key)

for value in dict_data.values():
    print(value) # value만 출력

''' Q12 '''
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)
    if x < 3:
        continue
    else:
        break

numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)
    if x >= 3:
        break

''' Q13 for-else '''
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)
    # if x >= 3:
    #     break
else:
    print("Perfect!")

''' Q14 while '''
x = 0
while x < 10:
    x += 1 # x = x + 1
    if x < 3:
        continue # 여기 걸리면 밑에거 실행 안됨 제발 기억해 stay!!!
    print(x)
    if x > 7:
        break

x = 1
total = 0
while True: # 그냥 계속 실행 킼
    total += x # total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x += 1

''' Q15 None'''
# NULL = None

a = None

if a is None:
    print("a is None")
elif a is not None:
    print("a is not None")