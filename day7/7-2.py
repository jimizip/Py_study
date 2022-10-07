# 1. 강의노트 “5 예외처리”의 p.7의 프로그램을 실행하고, 
# 출력 결과를 적고 설명하시오.
str = "89점"
try :
  score = int(str)
except ValueError : # ValueError 예외 발생 시 수행
  print("점수의 형식이 잘못됨")
except IndexError : # IndexError 예외 발생시 수행
  print("첨자가 범위를 벗어남")
else :
  print(score)