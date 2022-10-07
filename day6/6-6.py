# 1. 1부터 30까지의 서로 다른 난수 10개씩 생성하여 
# 리스트 A와 리스트 B를 만들고, 
# 이들의 교집합을 출력하는 프로그램을 작성하시오.
import random

a = []
b = []
for i in range(10):
  a.append(random.randint(1, 30))
  b.append(random.randint(1, 30))
print("a:", a)
print("b:", b)
print("교집합:")
for i in set(a):
  if i in b:
    print(i, end=' ')
