def func(a, b) :
      "이것은 함수의 도움말입니다"    # 몸체 첫 문자열은 함수의 도움말로 정의됨
      b, a = a, b
      return a, b

print(func)
print(type(func))
print(func.__doc__)              # __doc__ 은 함수에 정의된 도움말       

print(func(10,20))
c, d = func(1, 2)
print(c, d)
