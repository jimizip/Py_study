# 1. 강의노트 “5 예외처리”의 p.13의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
def some_function():
  print("1~10 사이의 수를 입력하세요:")
  num = int(input())
  if num < 1 or num > 10 :
    raise Exception("유효하지 않은 숫자입니다.: {0}".format(num))
  else :
    print("입력한 수는 {0}입니다.".format(num))
try:
  some_function()
except Exception as err:
  print("예외가 발생했습니다. {0}".format(err))
