# 1. 강의노트 p.25를 실행하고 결과를 적으시오.
def spam(eggs) :
  eggs = [2, 3]
  eggs.append(1)
  print(eggs)

ham = [0]
spam(ham)
print(ham)