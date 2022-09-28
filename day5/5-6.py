# 1. 강의노트 p.17을 참고하여 함수 2개를 리스트에 저장하여 호출하는 프로그램을 작성하고, 실행 결과를 보이시오.
def plus(a, b) :
  return a+b
def minus(a, b) :
  return a-b

myfunc=[plus, minus]
print(myfunc[0](1, 2))
print(myfunc[1](1, 2))
