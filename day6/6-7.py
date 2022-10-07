# 1. 10개의 쌍 (x, y)를 원소로 가지는 리스트를 반복문을 이용하여 만드시오. 
# 이때, x는 1에서 10까지 1씩 증가하는 정수이고, 
# y는 x의 거듭제곱이다. 
# 이 리스트를 이용하여 x와 y를 plot으로 그리시오.
import matplotlib.pyplot as m

x = [i for i in range(1, 11)]
y = [i ** 2 for i in x]

m.plot(x, y)
m.show()
