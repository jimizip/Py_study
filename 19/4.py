def var_key_args(**kwargs):
  print(type(kwargs))
  print(kwargs)

  for k, v, in kwargs.items():
    print("key =", k, "values=", v)

var_key_args()
var_key_args(a=1, b=2, c=3)

# 출력결과
# <class 'dict'>
# {}
# <class 'dict'>
# {'a': 1, 'b': 2, 'c': 3}
# key = a values= 1
# key = b values= 2
# key = c values= 3