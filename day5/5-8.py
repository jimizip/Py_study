# 1. 강의노트 p.24를 실행하고 결과를 적으시오.
def spam(eggs) :
  eggs.append(1)
  eggs = [2, 3] # ☞ 형식 매개변수 eggs와는 다른 객체 생성

ham = [0]
spam(ham)
print(ham)