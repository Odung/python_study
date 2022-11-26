# Factorial

def fact_iter(n):
    if n<0:
        raise ValueError("n should be larger than 1") # error, 프로그램 종료

    else:
        result = 1
        for number in reversed(range(1, n+1)):
            result *= number
        return result

print(fact_iter(6))

# n! = n*(n-1)!

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return fact_recursive(n-1) * n

print(fact_recursive(5))

# 함수 안에서 다시 같은 함수를 호출: recursion
# fact(4) -> 4*fact3 -> 4*3*fact(2) -> 4*3*2*fact(1) -> 4*3*2*1


# 과제~
# implement function which detects palindrome
# palindrome: 거꾸로 해도 같은 단어들, abcba, aaa (no space in input)

# if 문 사용
# def palindrome_iter(string):


def palindrome_iter(string):
    reverse_string = ''
    for i in string:
        reverse_string = i + reverse_string
    if string == reverse_string:
        print("word '%s' is a palindrome" %string)
    else:
        print("word '%s' is not a palindrome" %string)

palindrome_iter('kayak')
palindrome_iter('love')

def palidrome_iter2(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False

    return True

# recursion 사용
# base condition: 마지막에 대한 예외처리 하기 (함수가 끝남)

def palindrome_recursive(string):
    if len(string) == 0 or len(string) == 1: # base condition
        return True
    if string[0] == string[-1]:
        return palindrome_recursive(string[1:-1])
    else:
        return False

# 피보나치 수열의 n번째 항
# fibo(1) = 1, fibo(2) = 1, fibo(3) = 2(1+1), fibo(4) = 3(1+2) fibo(5) = 5(2+3)
# fibo(6) = 8(3+5)
# 1 1 2 3 5 8 13...

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(8))


# 하노이탑
def hanoi(N, start, mid, dest):
    if N == 1:
        print('%d -> %d' %(start, dest))
    if N == 2:
        print('%d -> %d' %(start, mid))
        print('%d -> %d' %(start, dest))
        print('%d -> %d' %(mid, dest))
    if N == 3:
        hanoi(N-1, start, dest, mid)
        print('%d -> %d' %(start, dest))
        hanoi(N-1, mid, start, dest)

def hanoi2(N, start, mid, dest):
    if N == 1:
        print('%d -> %d' %(start, dest))
    else:
        hanoi2(N-1, start, dest, mid)
        print('%d -> %d' %(start, dest))
        hanoi2(N-1, mid, start, dest)


hanoi2(1, 1, 2, 3)