# p.11의 프로그램에서 다음 내용을 수정하고, 실행한 결과를 보이시오.
#    - private 멤버로 __num 내용을 추가 
# (__init__   print_member 에 모두 반영) 
class TestPrivate :
  def __init__(self) :
    self.a = 100 
    self.__b = 200
    self.__num = 300
  def print_member(self) :
    print(self.a)
    print(self.__b)
    print(self.__num)

obj = TestPrivate()
obj.print_member()
print(obj.a)
print(obj.__b)
print(obj.__num)