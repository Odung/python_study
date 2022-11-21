# 3.2.2 계단 함수 구현하기
# 입력이 0을 넘으면 1 출력, 그 외에는 0을 출력

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# 넘파이 배열을 지원하도록
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
y = x > 0
print(y) # [false, true, true] # bool 배열
y = y.astype(np.int) # astype을 사용하여 bool을 int로 변환, [0 1 1] 출력
print(y)

def step_function(x):
    y = x > 0
    return y.astype(np.int)


# 3.2.3 계단 함수의 그래프
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = np.int) #dtype이용해서  type을 int로 바꿔줌

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
# plt.show()

# 0을 경계로 출력이 0에서 1로 바뀌므로 계단 함수


# 3.2.4 시그모이드 함수 구현하기
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

# broadcast기능 복습
t = np.array([1.0, 2.0, 3.0])
print(1.0 + t) # [2., 3., 4.] 출력
print(1.0 / t) # 1로 나눈 값을 출력

# 시그모이드 함수 그리기
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
# plt.show()


# 3.2.7 ReLU 함수
# 입력이 0을 넘으면 입력을 그대로 출력, 0이하이면 0을 출력
def relu(x):
    return np.maximum(0, x) # 두 입력 중 큰 값을 선택해 반환

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
# plt.show()

# 3.3 다차원 배열 계산
# 3.3.1 다차원 배열
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A)) # 배열의 차원 수 1
print(A.shape) # 배열의 형상 (4,)
print(A.shape[0]) # 4

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B)) # 2
print(B.shape) # (3, 2)


# 3.3.2 행렬의 내적(행렬 곱)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B)) # 행렬곱(내적)
# 행과 열의 원소 수 주의

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[7], [8]])
print(np.dot(A, B))

# 3.3.3 신경망의 내적
X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
print(np.dot(X, W))


# 3.4 3층 신경망 구현하기
x = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
print(A1)
Z1 = sigmoid(A1)

# 1층에서 2층으로
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 2층에서 3층으로
def identify_function(x):
    return x # 항등 함수(입력을 그대로 출력하는 함수)

W3 = np.array([[0.1, 0.3], [0.2, 0.3]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identify_function(A3)

# 3.4.3 구현 정리
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identify_function(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)


# 3.5 출력층 설계하기
# 3.5.1 항등 함수와 소프트맥스 함수 구현하기
# 항등 함수: 입력을 그대로 출력

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum(exp_a)
print(y)


def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

# 오버플로우: 입력 신호 중 최댓값을 빼주면 올바른 계산 가능
# 아래는 오버플로우를 방지하는 소프트맥스 함수
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))