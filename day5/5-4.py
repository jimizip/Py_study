# 1. 강의노트 p.15를 참고하여 다음의 프로그램을 작성하고, 실행 결과를 보이시오.
# - 키보드로 정수 1개를 입력받아, 함수 factorial()을 호출하여 반환 값을 출력한다.

def factorial(n) :
  if n == 0:
    return 1
  elif n > 0 :
    return factorial(n-1)*n

print("정수 1개를 입력하세요: ")
a = int(input())
print("결과:" , factorial(a))