# p.12의 MyClass의 클래스 변수를 수정하는 예이다. 다음 내용을 실행하고 결과를 보이시오.
# 	print(MyClass.var)
# 	MyClass.var = "잘가"
# 	print(MyClass.var)
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
MyClass.var = "잘가"
print(MyClass.var)
