# 5. 다음은 Person 클래스의 일부이다. 
# 제시된 내용대로 완성하시오.
class Person:
 def __init__(self, name, height, weight):
#  name, height, weight 값을 매개변수로 받아 초기화
  self.name = name
  self.height = height
  self.weight = weight

 def print_info (self):
#  name, height, weight 값을 출력
  print("이름: " + self.name + " 키: " + str(self.height) + " 몸무게: " + str(self.weight))

 def is_fat(self):
#  비만도를 판정하는 메소드
#  비만도 : height - 100 < weight이면 비만
  if(self.height - 100 < self.weight):
    print("비만입니다.")
  else:
    print("비만이 아닙니다.")

kim = Person("박다흰", 180, 79)
kim.print_info()
kim.is_fat()