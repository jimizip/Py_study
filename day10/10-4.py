# 오버라이딩을 사용하는 프로그램이다. 빈 칸에 다음 내용을 작성하고, 실행한 결과를 보이시오.
#    - “안녕하세요. 반갑습니다”를 출력함
#    - 단, “안녕하세요”는 super()를 사용하여 출력함
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
      super().greeting()
      print('반갑습니다')

kim = Student()
kim.greeting()
