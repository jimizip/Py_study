# 1. 강의노트 “5 예외처리”의 p.5의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
str = "89점"
try :
  score = int(str)
except :
  print("예외가 발생")
else :
  print(score)