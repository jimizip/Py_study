# 위 3번을 참고하여, 
# 두 개 리스트에 있는 요소 중에서 중복된 요소만 구해서 리스트로 만드는 프로그램을 작성하시오.
a = [1, 2, 3]
b = [3, 4, 5]
c = []
for item in a :
  if item in b :
    c.append(item)
print("중복된 요소: ", c)
