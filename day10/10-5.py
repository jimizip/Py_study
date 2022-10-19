# 강의노트 p.28의 프로그램을 변경하여 __str__() 메소드의 사용 예를 작성하고 실행한 결과를 보이시오.
class School :
  def __init__(self, class_name, stu_name) :
    self.class_name = class_name
    self.stu_name = stu_name
  def __str__(self) :
    return "과목명: %s, 학생이름: %s"%(self.class_name, self.stu_name)

koo = School("공개SW","구지민")
print(koo) # 객체 kim을 print -> __str__ 메소드가 호출됨
koo = School("팀프1", "구지민")
print(koo)
