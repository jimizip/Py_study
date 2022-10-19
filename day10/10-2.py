# 다음 내용이 포함된 클래스를 작성하고, 메소드를 호출하고 실행하는 예를 보이시오.
#    - 클래스 멤버 money : 돈 잔액 (초기값은 0)
#    - 클래스 메소드 change_money : 전달하는 매개변수 값으로 돈 잔액을 증가 또는 감소
#    - 클래스 메소드 print_money : 돈 잔액 값 출력
# (시험출제가능)
class Money :
  money = 0
  @classmethod
  def change_money(cls, change_money) :
    cls.money += change_money

  @classmethod
  def print_money(cls) :
    print(cls.money)

a = Money()
Money.change_money(1000)
Money.print_money()
Money.change_money(-300)
Money.print_money()