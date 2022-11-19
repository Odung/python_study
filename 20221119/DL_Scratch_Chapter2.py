# 2.3 퍼셉트론 구현하기
# 2.3.1 간단한 구현부터

# AND GATE
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1))

# 2.3.2 가중치와 편향 도입

import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w*x) # array([0., 0.5])
print(np.sum(w*x) + b) # -0.19999999

# 가중치와 편향을 도입한 AND GATE

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b # np.dot(w, x) 내적~ w @ x 내적~?
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0, 0), AND(0, 1), AND(1, 0), AND(1, 1))

# NAND GATE (1, 1)일 때만 0을 출력
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.dot(w, x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(NAND(0, 0), NAND(0, 1), NAND(1, 0), NAND(1, 1))

# OR GATE
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.dot(x, w)
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0, 0), OR(0, 1), OR(1, 0), OR(1, 1))


# 2.4 퍼셉트론의 한계
# 2.4.1 도전! XOR GATE
# 선형으로 구현 불가능(AND, NAND, OR은 선형으로 구현 가능)
def XOR(x1, x2):
    s1 = NAND(x1, x2) # 위에서 정의된 친구들을 가져옴 룰루
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
# 이것이 바로 다층 퍼셉트론 !! 우와~~ 신기해용~~

print(XOR(0, 0), XOR(0, 1), XOR(1, 0), XOR(1, 1))