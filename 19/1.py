# 문자열의 슬라이싱 기능을 이용하여 프로그램을 작성하시오.
txt1 = 'aAbBcCdDeEfFgGhH'
txt2 = 'abcdefghijk'
print(txt1[::2]) # abcdefgh 2칸씩 오른쪽으로 이동하면서 가져오기
print(txt2[-1:-12:-1]) #kjihgfedcba 
print(txt2[::-1]) # kjihgfedcba

# a[start : end : step]
# start: 슬라이싱을 시작할 시작위치입니다.
# end: 슬라이싱을 끝낼 위치로 end는 포함하지 않습니다!
# step: stride(보폭)라고도 하며 몇개씩 끊어서 가져올지와 방향을 정합니다. 옵션이며 아래의 예제를 확인하면 쉽게 이해가 가능합니다.
# step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져옵니다.
# step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져옵니다.