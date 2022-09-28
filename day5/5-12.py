# 두 개의 숫자를 매개변수로 받아서 두 숫자에 공통된 숫자를 출력하는 함수 same_number()를 작성하시오. 
# 예를 들어, 38472 와 173 의 경우 [3, 7]이 출력됨.
def same_number( num_a, num_b ):
  num_a = list(str(num_a))
  num_b = list(str(num_b))
  result = []
  for i in num_a:
    if i in num_b:
      result.append(int(i))
  return result

print("첫번째 정수를 입력하세요: ")
a = int(input())
print("두번째 정수를 입력하세요: ")
b = int(input())
print(same_number(a,b))