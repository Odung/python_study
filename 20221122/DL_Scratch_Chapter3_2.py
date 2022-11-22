from mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
# 아직 DATA를 불러오기만 한 것임^^..

# 이미지 확인하기
import numpy as np
from PIL import Image # 이미지와 관련된 기능

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_train[0]
label = t_train[0]
print(label) # 5

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

# img_show(img)


# 3.6.2 신경망의 추론 처리
# 입력층 뉴런 784개, 출력층 10개, 은닉층 2개

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

import pickle
def get_data():
    _, (x_test, t_test) = \
    load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network(): # 학습이 완료된 weight를 가져옴(가중치와 편향을 적절히 조정한 친구를 데려옴)
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

# 60000장은 여기서 안씀
def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1) # 충격 np에 없다고 한다 그렇다...
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    # print("before softmax", a3)
    y = softmax(a3)
    # print("after softmax", y)

    return y

x, t = get_data()
network = init_network()
print(network.keys())
print(network['W1'].shape)
print(network['b1'].shape)

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print(float(accuracy_cnt)/len(x))


# 3.6.3 배치 처리
x, t = get_data()
network = init_network()

batch_size = 100 # 배치 크기
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i : i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis = 1)
    accuracy_cnt += np.sum(p == t[i : i+batch_size])
    # print(y_batch.shape)

print(x.shape)
print(float(accuracy_cnt)/len(x))