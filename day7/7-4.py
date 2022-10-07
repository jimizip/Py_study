# 1. 강의노트 “5 예외처리”의 p.10의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
def calsum(n) :
  if (n < 0) :
    raise ValueError # 예외 이름 없이 raise 만 사용해도 됨
  sum = 0
  for a in range(n+1) :
    sum += a
  return sum
try :
  print(calsum(10))
  print(calsum(-5))
except :
  print("입력값이 잘못됨")