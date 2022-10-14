# 1. 강의노트 “6. 파일다루기” p.21의 연습문제를 푸시오.
# 1 파일에서 특정 단어를 다른 단어로 교체하는 프로그램을 작성하시오.
# 예를 들어, “abc”를 “111”로 대체시킴.
# 파일 이름과 단어 2개는 키보드로 입력받는다.
file_name = input("파일 이름을 입력하세요: ")
word_name = input("바꾸기 전 단어를 입력하세요: ")
after_word_name = input("바꾸고 난 후 단어를 입력하세요: ")

with open(file_name, "r") as f :
  text = f.read()

with open(file_name, "w") as f :
  text = text.replace(word_name, after_word_name)
  f.write(text)

# 2 Zip 파일의 압축을 푸는 프로그램을 작성하시오.
# (hint) p.20 프로그램의 6번째줄에서 
# ziph.write() 대신에 ziph.extractall() 사용
from fileinput import filename
import zipfile

def compressZip(zipname, filename) : 
  print("[%s] -> [%s] 압축 풀기...." %(zipname, filename))
  with zipfile.ZipFile(zipname, 'r') as ex :
    ex.extractall(filename)
  
  print("압축이 풀렸습니다.")

zipname = input("압축을 풀 파일이름을 입력하세요: ")
filename = input("압축이 풀린 파일의 이름을 입력하세요: ")
compressZip(zipname, filename)

# 3 파일에서 알파벳의 개수를 구하는 프로그램을 작성하시오.
# 파일 이름은 키보드로 입력받는다
file_name = input("파일 이름을 입력하세요: ")
alpha = 'abcdefghijklmnopqrstuvwxyz'
alphabet = [0] * 26
with open(file_name, "r") as f:
  text = f.read()
  text = text.lower()
  for a in text:
    if a in alpha:
      i = alpha.find(a)
      alphabet[i] += 1
  
print("알파벳 개수")
for i in range(0,26):
  print(alpha[i], ":", alphabet[i])
