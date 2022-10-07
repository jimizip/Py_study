# 1. 원의 반지름을 사용자 입력으로 받아 
# 원의 면적을 출력하는 프로그램을 작성하시오.
import numpy as n

print("반지름을 입력하세요: ")
a = int(input())
print("면적:", a ** 2 * n.pi)
