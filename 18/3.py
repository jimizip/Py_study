from ast import keyword
import keyword

# 모듈 keyword 의 keyword.kwlist 는 
# python의 키워드 리스트이다. 
# 사용자로부터 문자열을 입력받아 
# python의 키워드인지 아닌지 여부를 출력하시오.
print('python의 키워드:')
print(keyword.kwlist)

word = input('문자열을 입력하세요:')
if (keyword.iskeyword(word) == 1) :
  print('python의 키워드이다.')
else:
  print('python의 키워드가 아니다.')
