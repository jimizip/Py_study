# 행렬 A와 B를 다음과 같이 정의하시오.
#  A = [[1, 4],
#  [2, 5], 
#  [3, 6]]
#  B = [[12, 11, 10],
#  [7, 6, 5]]
#  두 행렬의 행렬곱을 구하는 함수를 정의하시오. 
# 이 함수를 호출하여 AB를 계산하고 행렬 AB 값을 출력하시오

def Cal(A, B):
  gop = 0
  result = 0
  an = []
  for i in range(3):
    answer = []
    for k in range(0,3):
      result = 0
      for j in range(0,2):
        gop = (A[i][j]*B[j][k])
        result = result + gop
      answer.append(result)
    an.append(answer)
  return an

a = [[1, 4],[2, 5], [3, 6]]
b = [[12, 11, 10],[7, 6, 5]]
print("계산 결과: {0}".format(Cal(a,b)))