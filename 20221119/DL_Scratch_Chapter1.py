# 우와 딥러닝을 시작했당
import numpy as np

x = np.array([1, 2, 3, 4, 5]) # numpy array
print(x)
# numpy에 있는 함수를 쓰러면 numpy.array를 넘겨줘야 함!!
# 내부에 있는 요소끼리 연산 가능해짐

# 행렬 만들기 가능
A = np.array([
    [1, 3],
    [2, 4]
])

print(A[0,0]) # 0행 0열

# Shape
print(A.shape) # 2X2 행렬 (2, 2) 출력
img = np.random.rand(3, 32, 32) # channel, height, width 순서로 입력
print(img.shape)

B = np.array([
    [3, 0],
    [0, 6]
])

print(A + B)
print(A * B) # 같은 위치에 있는 요소끼리 곱한 결과가 나옴(element-wise mutuplication)

# 그렇다면 행렬곱은 어떻게 ?!
print(np.dot(A, B))
print(A @ B)

print(A * 10) # Broadcast, 각 요소에 곱해줌

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

B = np.array([10, 20])
print(A * B)

# [10, 40], [30, 80], [50, 120] 요러케 출력

print(A.flatten()) # 1, 2, 3, 4, 5, 6출력

A = A.flatten()
print(A[[1, 3, 5]]) # 대괄호 한번 더 씌우면 여러개 뽑아줌
print(type(A))

# 조건 달기, n차원 확장해도 가능
print(A[A>3])
print(A>3)

# 그래프그리기 우왕너무기대돼!!!!!

import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend() # label에서 입력한것이 legend로 들어감
plt.show()

# 이미지 불러오기
from matplotlib.image import imread

img = imread("C:\\Users\\user\\Desktop\\KakaoTalk_20221119_201043287.png")
plt.imshow(img)
plt.show()