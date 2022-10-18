# p.17의 연습문제 3개를 풀고, 실행한 결과를 보이시오.
# 1. 앞에서 만든 Human 클래스에서 __equ__ 메소드는 이름과 
# 나이가 모두 같은 지를 반환해주고 있다. 
# 나이는 제외하고 이름만 같은 지를 반환하도록 수정하시오.
# class Human :
#   def __init__(self, age, name) :
#     self.age = age
#     self.name = name
#   def __eq__(self, other) :
#     return self.name == other.name
# kim = Human(29,"홍길동")
# sang = Human(29,"홍길동")
# moon = Human(30,"이순신")
# print(kim==sang)
# print(kim==moon)
# 2. Human 클래스에서 __le__ 메소드를 다음과 같이 추가하시오. 
# self의 나이가 other의 나이보다 작거나 같은 지를 반환함.
# class Human :
#   def __init__(self, age, name) :
#     self.age = age
#     self.name = name
#   def __eq__(self, other) :
#     return self.age == other.age and self.name == other.name
#   def __le__(self, other) :
#     return self.age <= other.age

# kim = Human(29,"홍길동")
# sang = Human(29,"홍길동")
# moon = Human(30,"이순신")
# print(kim==sang)
# print(kim==moon)
# 3. 앞의 프로그램에서, 1 + kim 을 하면 kim의 나이에 
# 1을 추가하도록 구현하시오. 
# 이를 위해, __radd__ 메소드를 추가해야 함
class Human :
  def __init__(self, age, name) :
    self.age = age
    self.name = name
  def __eq__(self, other) :
    return self.age == other.age and self.name == other.name
  def __le__(self, other) :
    return self.age <= other.age
  def __radd__(self, plus) :
    return self.age + plus

kim = Human(29,"홍길동")
sang = Human(29,"홍길동")
moon = Human(30,"이순신")
print(kim==sang)
print(kim==moon)
print(1+kim)
