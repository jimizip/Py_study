# 1. 강의노트 “6. 파일다루기”의 p.15 – p.16의 프로그램을 실행하고, 출력결과를 적고 설명하시오.
# 15p-1
import shutil
shutil.copy("hello.txt", "hello2.txt")
# 15p-2
import os
os.mkdir("log")
# #16p
# import os
folder = '.'
file_list = os.listdir(folder)
print(file_list)