#  p.13 프로그램의 실행 결과를 적고, 출력된 결과를 각각 설명하시오.
class CalCounter :
  count = 0 # 클래스 멤버
  def __init__(self) :
    CalCounter.count += 1 # 클래스 멤버인 count의 값을 접근
  def print_count(self) :
    print(self.count)

a = CalCounter()
a.print_count()
b = CalCounter()
b.print_count()
