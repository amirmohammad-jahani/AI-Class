import random
import math
import matplotlib.pyplot as plt

apple_width  = [random.uniform(7, 9) for _ in range(50)]
apple_height = [random.uniform(7, 9) for _ in range(50)]

banana_width  = [random.uniform(3, 5) for _ in range(50)]
banana_height = [random.uniform(15, 20) for _ in range(50)]

x_train = []
y_train = []

for i in range(50):
    x_train.append([apple_width[i], apple_height[i]])
    y_train.append(0) 

for i in range(50):
    x_train.append([banana_width[i], banana_height[i]])
    y_train.append(1)

new_fruit = [7.5, 8.5]

distance = []
for fruit in x_train:
    d = math.sqrt((fruit[0] - new_fruit[0])**2 + (fruit[1] - new_fruit[1])**2)
    distance.append(d)

plt.scatter(apple_width, apple_height, color='red', label='Apple')
plt.scatter(banana_width, banana_height, color='yellow', label='Banana')

plt.scatter(new_fruit[0], new_fruit[1], color='blue', s=150, label='New Fruit')

plt.xlabel('Width')
plt.ylabel('Height')
plt.legend()
plt.show()