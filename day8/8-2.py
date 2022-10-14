# 1. 강의노트 “6. 파일다루기”의 p.17 – p.20의 프로그램을 실행하고, 출력결과를 적고 설명하시오.
# 17p
import os
import random, datetime
if not os.path.isdir("log") :
  os.mkdir("log")
if not os.path.exists("log/count_log.txt") :
  f = open("log/count_log.txt", "w")
  f.write("기록 시작\n")
  f.close()
with open("log/count_log.txt", "a") as f :
  for i in range(1, 11) :
    stamp = str(datetime.datetime.now())
    value = random.random() * 1000000
    log_line = stamp + "\t" + str(value) + "값이 생성됨" + "\n"
    f.write(log_line)
# 18p
with open("log/count_log.txt", "r") as f :
  text = f.read()
  word_list = text.split(" ") # 빈 칸 기준으로 단어를 분리
  line_list = text.split("\n") # 한 줄씩 분리
print("총 글자의 수: ", len(text))
print("총 단어의 수: ", len(word_list))
print("총 줄의 수: ", len(line_list))
# 19p
file_name = input("파일 이름을 입력하시오: ")
word_name = input("찾을 단어를 입력하시오: ")

with open(file_name, "r") as f :
  text = f.read()
  text = text.lower()
  pos = text.find(word_name)
  count = 0
  while pos != -1 :
    count += 1
    pos = text.find(word_name, pos+1)

print("개수는", count)
# 20p
import zipfile

def compressZip(zipname, filename) :
  print("[%s] -> [%s] 압축...." %(filename, zipname))
  with zipfile.ZipFile(zipname, 'w') as ziph :
    ziph.write(filename)
  print("압축이 끝났습니다")

filename = input("파일이름을 입력하시오: ")
zipname = filename + '.zip'
compressZip(zipname, filename)