# 1. 강의노트 “5 예외처리”의 p.12의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
str = "89점"
try :
  score = int(str)
except ValueError as e :
  print(e)
else :
  print(score)
finally :
  print("무조건 수행합니다")