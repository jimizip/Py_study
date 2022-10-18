#  p.12 프로그램의 실행 결과를 적고, 
# 출력된 결과를 각각 설명하시오.
class MyClass :
  var = "안녕하세요!!" # 클래스 멤버
  def sayHello(self) :
    msg1 = "안녕"
    self.msg2 = "Hi"
    print(msg1)
    print(self.var) # 객체의 var를 새로 정의하여 사용

obj = MyClass()
print(obj.var) # 객체를 통한 클래스 멤버 접근
obj.sayHello() # 객체의 메소드를 통한 접근
print(MyClass.var) # 클래스 이름으로 접근
