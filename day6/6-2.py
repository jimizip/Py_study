# 1. 강의노트 “4 모듈과 패키지”의 p.19 – p.21의 프로그램을 실행하고, 출력 결과를 적고 설명하시오.
#19p
import matplotlib.pyplot as plt
# 0~10까지 x, y에 대입
x=y=[i for i in range(0, 11)]
plt.plot(x, y) 
plt.show()
#20p
import numpy as np
import matplotlib.pyplot as plt
# 사인곡선에 해당하는 x와 y 좌표를 계산
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
# matplotlib를 사용해 점들을 표시
plt.plot(x, y) 
plt.show()
#21p
from urllib import request
import bs4
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs4.BeautifulSoup(target, "html.parser")
for city in soup.select("location") :
  name = city.select_one("city").string
  wf = city.select_one("wf").string
  tmn = city.select_one("tmn").string
  tmx = city.select_one("tmx").string
  print(name, ': ', wf, '(', tmn, '~', tmx, ')')