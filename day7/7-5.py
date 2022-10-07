# 1. 강의노트 “5 예외처리”의 p.11의 두번째 프로그램을 실행하고,
#  출력 결과를 적고 설명하시오.
text = input()
if text.isdigit() == False :
  try :
    raise Exception("입력 문자열이 숫자가 아닙니다.")
  except Exception :
    print("예외가 일어났습니다.")
