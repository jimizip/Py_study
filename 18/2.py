# 두 개의 문자열을 입력받아 
# 길이가 짧은 문자열을 
# 결정(또는 반환)하는 함수를 정의하시오.
# 사용자로부터 5개의 문자열을 입력받아
# 리스트에 저장한다.
# 저장된 리스트에서 가장 길이가 
# 짧은 문자열을 찾아 출력하시오.
# 이때 문제에서 정의한 함수를 사용하시오.

# 1번째 방법
def StringL():
  strFive = list(input('5개의 문자열을 입력하세요:').split())
  min_str = min(strFive, key = len)
  print(min_str)

StringL()

# 2번째 방법
def StringL2():
  strs = list(input('5개의 문자열을 입력하세요:').split())
  minStr = strs[0]
  for i in range(5):
    if len(minStr) > len(strs[i]):
      minStr = strs[i]
  print(minStr)

StringL2()

# 3번째 방법
def StringL3(list):
  minStr = list[0]
  for i in range(len(list)):
    if len(minStr) > len(list[i]):
        minStr = list[i]
  print(minStr)

strs = list(input('5개의 문자열을 입력하세요:').split())
StringL3(strs)

# 4번째 방법
def StringL4(list):
  minStr = min(list, key=len)
  print(minStr)

strs4 = list(input('5개의 문자열을 입력하세요:').split())
StringL4(strs4)
