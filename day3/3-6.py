# 1. 빈 리스트를 만든 후, 키보드로 5개의 양수 숫자를 입력받아 리스트에 저장하시오. 리스트의 값 중에서 최댓값과 최솟값을 구하는 프로그램을 작성하고, 실행 결과를 적으시오.
print('양수 5개를 입력하세요: ')
a = []
for data in range(5):
  data = int(input())
  a.append(data)
for i in range(5):
  a.sort()
print("최솟값: ", a[0])
print("최댓값: ", a[4])