# 1. 강의노트 “5 예외처리”의 
# p.14의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is", result)
  finally:
    print("executing finally clause")

divide(2,1)
divide(2,0)
divide("2","1")