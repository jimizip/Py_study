# 문자열 “a:b:c:d”가 있다. 문자열의 replace 함수를 사용하여 “a#b#c#d”로 바꿔서 출력하는 프로그램을 작성하시오.

str1 = "a:b:c:d"
str2 = str1.replace(':', '#')
print(str2)
