# 1. 강의노트 p.8을 참고하여 다음의 프로그램을 작성하고, 실행 결과를 보이시오. 5개의 숫자를 키보드로 입력받아, 함수 intsum()을 호출하여 합을 구해서 출력한다.
def intsum( *ints ):
  sum = 0
  for s in ints:
    sum += s
  return sum

print("첫번째 숫자를 입력하세요: ")
a = int(input())
print("두번째 숫자를 입력하세요: ")
b = int(input())
print("세번째 숫자를 입력하세요: ")
c = int(input())
print("네번째 숫자를 입력하세요: ")
d = int(input())
print("다섯번째 숫자를 입력하세요: ")
e = int(input())
print("합은",intsum(a, b, c, d, e), "입니다.")

# print('5개의 숫자를 입력하세요: ')
# a = []
# for i in range(5):
#   i = int(input())
# a.append(i)
# print(a)
# print('합은 ', intsum(a))

