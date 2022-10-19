# 강의노트 p.23을 실행하고, 출력 결과를 보이시오.
class BaseA :
  def __init__(self) :
    print('BaseA.__init__()')

class B(BaseA) : 
  def __init__(self) :
    print('B.__init__()')
    super().__init__() 

b = B()