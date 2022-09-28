# 1. 강의노트 p.7을 실행하고 결과를 적으시오.
def print_string (*mytext) :
  result = ''
  for s in mytext:
    result = result + s
  return result
  
print(print_string('파이썬은', '정말', '재미있다'))