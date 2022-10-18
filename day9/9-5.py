# p.12의 MyClass의 sayHello 메소드에서 맨 마지막 줄에 다음 내용을 추가하시오. 
#         self.var = “Hello World”
# MyClass의 객체 obj를 생성한 후, 
# sayHello 메소드를 호출한 뒤, 
# obj.var 값과 MyClass.var 값을 print 하시오.
# 출력된 결과를 설명하시오.
class MyClass :
  var = "안녕하세요!!" # 클래스 멤버
  def sayHello(self) :
    msg1 = "안녕"
    self.msg2 = "Hi"
    print(msg1)
    print(self.var) # 객체의 var를 새로 정의하여 사용
    self.var = "Hello World"

obj = MyClass()
print(obj.var) # 객체를 통한 클래스 멤버 접근
obj.sayHello()
print(obj.var) # 객체를 통한 클래스 멤버 접근
print(MyClass.var) # 클래스 이름으로 접근
