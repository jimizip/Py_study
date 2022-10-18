# p.7의 프로그램에서 다음 내용을 수정하고, 실행한 결과를 보이시오.
#    - class Player에 self.weight 내용을 추가 
# (__init__   print_info 에 모두 반영)
#    - Player 객체 생성할 때, weight 값을 75로 함
class Player :
  def __init__(self, name, height, weight) :
    self.number = 100
    self.name = name
    self.height = height
    self.weight = weight
  def print_info(self) : 
    print(self.number)
    print(self.name)
    print(self.height)
    print(self.weight)

a = Player('gildong', '178', '75')
a.print_info()