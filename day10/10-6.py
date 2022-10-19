# 강의노트 p.29의 프로그램을 변경하여 __call__() 메소드의 사용 예를 작성하고 실행한 결과를 보이시오.
class sayMyName :
  def __init__(self) :
    print('구지민~')
  def __call__(self) :
    print('넵!')

koo = sayMyName() # 객체를 생성  __init__ 호출  A를 출력
koo() # __call__() 호출