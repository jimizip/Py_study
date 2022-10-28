# 다음은 Person 클래스의 일부이다. 제시된 내용대로 완성하시오.
class Person:
 def __init__(self, name, height, weight):
  #  name, height, weight 값을 매개변수로 받아 초기화
  self.name = name
  self.height = height
  self.weight = weight
 
 def print_info(self):
  #  name, height, weight 값을 출력
  print("name: " + self.name + " height: " + str(self.height) + " weight: " + str(self.weight))

koo = Person("구지민", 160, 45)
koo.print_info()