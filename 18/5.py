# 문제 5의 Person 클래스에 비만도를 판정하는 메소드를 추가하시오.
# 비만도: height - 100 < weight 이면 비만
# '철수'의 키(height)와 체중(weight)을 입력받아
# 비만여부를 출력하시오. 정의한 Person 클래스를 사용하시오.
class Person:
  def __init__(self, name, height, weight):
    #  name, height, weight 값을 매개변수로 받아 초기화
    self.name = name
    self.height = height
    self.weight = weight
  
  def print_info(self):
    #  name, height, weight 값을 출력
    print("name: " + self.name + " height: " + str(self.height) + " weight: " + str(self.weight))
  
  def biman(self):
    if self.height - 100 < self.weight:
      print("비만입니다")
    else:
      print("비만아니다")

koo = Person("구지민", 159, 48)
koo.print_info()
koo.biman()