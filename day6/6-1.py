# 1. 강의노트 “4 모듈과 패키지”의 p.8 – p.14의 
# 프로그램을 실행하고, 출력 결과를 적고 설명하시오.
#8p
import sys
print("version = ", sys.version) # 파이썬 버전
print("platform = ", sys.platform) # OS (윈도우의 경우 win32 출력)
print("path = ", sys.path)
#9p
import time
t = time.time() # 1970년 이후 지나온 시간을 초로 출력
# 소수점은 나노 초(nano second) 까지
print(t)
print(time.ctime(t)) # 년도, 월, 일, 요일, 시간으로 변환 출력
print(time.localtime(t)) # struct_time 형식으로 변환 출력
start = time.time()
for a in range(100) :
  print(a, end=',')
print()
end = time.time()
print(end - start)
#10p
import random
for i in range(5) :
  print(random.random()) # 난수 생성
for i in range(5) :
  print(random.randint(1, 10)) # 1 ~ 10 중의 정수 난수를 생성
for i in range(5) :
  print(random.uniform(1, 10)) # 1 ~ 10 중의 실수 난수를 생성
food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food)) # food 리스트에서 하나를 무작위 선택
print(random.sample(food, 2)) # food 리스트에서 2개를 선택
random.shuffle(food) # food 리스트의 요소를 무작위 섞음
print(food)
#11p
import statistics
score = [30, 40, 50, 60, 70, 90]
print(statistics.mean(score))
print(statistics.median(score))
print(statistics.stdev(score))
print(statistics.variance(score))
#12p
import turtle as t
t.shape("turtle") # 이동체의 모양 지정 (turtle, circle 등)
t.right(60) # 오른쪽으로 60도 방향 설정
t.forward(100) # 100 픽셀의 거리를 이동
t.right(120) # 오른쪽으로 120도 방향 설정
t.forward(100)
t.right(120)
t.forward(100)
t.done()
#13p
import turtle as t
t.shape("turtle")
for a in range(5) :
  t.forward(150)
  t.right(144)
t.done()
#14p
import turtle as t
t.shape("turtle")
t.pensize(3)
t.color("blue")
t.bgcolor("green")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.done()
