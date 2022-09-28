# 다음 프로그램은 내장함수들을 연습한다. 출력 결과를 적고 설명하시오.
a = sum([1,2,3,4])
b = sum([1,2,3,4], 5)
print(a,b)

s = "a = a + 100"
a = 100
exec(s)
print(a)

k = ['abc', 'bc', 'a']
print(sorted(k))
print(sorted(k, reverse=True))

s = "IwantotoknowPython "
print(ord(s[0]))
a = list(map(ord, s))
print(a)
aa = list(map(chr, a))
print(aa)
