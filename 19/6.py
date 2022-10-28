# 6. class Person을 상속하는 Student 클래스 만들기
#  __init__메소드를 추가하여 이름, 키, 몸무게, 전화번호, 학교
# 를 초기화. 이름, 키, 몸무게는 class Person의 __init__을 
# 호출하여 초기화하시오.
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

class Student(Person):
  def __init__(self, name, height, weight, phone, school):
    self.phone = phone
    self.school = school
    super().__init__(name, height, weight)
  def print_info(self):
    print("이름: " + self.name + " 키: " + str(self.height) + " 몸무게: " + str(self.weight) + " 전화번호: " + str(self.phone) + " 학교: " + self.school)

kim = Person("박다흰", 180, 78)
kim.print_info()
kim.is_fat()
park = Student("박다흰", 180, 78, 3676, "명지대학교")
park.print_info()